from django.shortcuts import render
from .forms import EncryptForm, DecryptForm
from .logic import generate_key, encrypt_message, decrypt_message
import base64

def encrypt_view(request):
    encrypted_message = key = None
    if request.method == 'POST':
        form = EncryptForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            key = generate_key()
            encrypted_message = encrypt_message(message, key)
            key = key.decode()
            encrypted_message = encrypted_message.decode()
    else:
        form = EncryptForm()
    return render(request, 'encrypt.html', {
        'form': form,
        'encrypted_message': encrypted_message,
        'key': key
    })

def decrypt_view(request):
    decrypted_message = None
    if request.method == 'POST':
        form = DecryptForm(request.POST)
        if form.is_valid():
            enc_msg = form.cleaned_data['encrypted_message']
            key = form.cleaned_data['key']
            try:
                decrypted_message = decrypt_message(enc_msg, key)
            except Exception as e:
                decrypted_message = f"Erreur de déchiffrement: {str(e)}"
    else:
        form = DecryptForm()
    return render(request, 'decrypt.html', {
        'form': form,
        'decrypted_message': decrypted_message
    })