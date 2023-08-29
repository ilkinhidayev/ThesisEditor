from django.shortcuts import render, redirect
from .forms import TezForm
from .models import Tez
from .utils.docx_converter import convert_to_guidelines
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
import os

@login_required  # Tez yüklemek için kullanıcının giriş yapmış olması gerektiğini belirtiyoruz.
def tez_yukle(request):
    if request.method == 'POST':
        form = TezForm(request.POST, request.FILES)
        if form.is_valid():
            tez = form.save(commit=False)  # Veritabanına kaydetmeden önce nesneyi al
            tez.owner = request.user  # Tezi şu anda giriş yapmış olan kullanıcıya ata
            tez.save()  # Tezi veritabanına kaydet
            converted_path = convert_to_guidelines(tez.dosya.path)
            tez.dosya_converted = converted_path.replace('media/', '')
            tez.save()
            return redirect('user_tezleri')
    else:
        form = TezForm()
    return render(request, 'Thesis/tez_yukle.html', {'form': form})



def tez_listesi(request):
    tezler = Tez.objects.filter(owner=request.user) # sadece oturum açmış olan kullanıcının tezlerini getir
    return render(request, 'Thesis/tez_listesi.html', {'tezler': tezler})


def delete_tez(request, tez_id):
    tez = Tez.objects.get(id=tez_id)

    # Kullanıcının bu teze sahip olup olmadığını kontrol edin
    if tez.owner != request.user:
        messages.error(request, "Bu tezi silme yetkiniz yok!")
        return redirect('user_tezleri')

    # Tezin dosyalarını silme
    dosya_path = os.path.join(settings.MEDIA_ROOT, str(tez.dosya))
    if os.path.exists(dosya_path) and dosya_path.startswith(settings.MEDIA_ROOT):
        tez.dosya.delete()

    if tez.dosya_converted:
        dosya_converted_path = os.path.join(settings.MEDIA_ROOT, str(tez.dosya_converted))
        if os.path.exists(dosya_converted_path) and dosya_converted_path.startswith(settings.MEDIA_ROOT):
            tez.dosya_converted.delete()

    tez.delete()  # Bu tezin veritabanından kaydını siler
    return redirect('user_tezleri')


@login_required
def user_area(request):
    return render(request, 'user_area.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, hesabınız başarıyla oluşturuldu! Şimdi giriş yapabilirsiniz.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def user_tezleri(request):
    tezler = Tez.objects.filter(owner=request.user)
    return render(request, 'user_tezleri.html', {'tezler': tezler})

def custom_logout(request):
    logout(request)
    return redirect('ana_sayfa_url_name')  # 'ana_sayfa_url_name' yerine ana sayfanızın URL adını yazın.