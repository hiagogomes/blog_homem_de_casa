from django.shortcuts import render, redirect
from .forms import ContatoForm

def home(request):
    return render(request, 'blog/home.html')

def sobre(request):
    return render(request, 'blog/sobre.html')

def politica_privacidade(request):
    return render(request,'blog/politica_privacidade.html')

def politica_afiliado(request):
    return render(request,'blog/politica_afiliado.html')

def termos_uso(request):
    return render(request, 'blog/termos_uso.html')

def contato(request):
    sucesso = False

    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            sucesso = True
            form = ContatoForm()  # limpa o formulário após o envio
    else:
        form = ContatoForm()

    return render(request, 'blog/contato.html', {'form': form, 'success': sucesso})

def playstation(request):
    return render(request, 'blog/posts/playstation.html')

def relogios(request):
    return render(request, 'blog/posts/relogios.html')

def parafusadeira(request):
    return render(request, 'blog/posts/parafusadeira.html')

def panelas(request):
    return render(request, 'blog/posts/panelas.html')

def airfryer(request):
    return render(request, 'blog/posts/airfryer.html')

def fones(request):
    return render(request, 'blog/posts/fones.html')

def echopop(request):
    return render(request, 'blog/posts/echopop.html')

def lavadora(request):
    return render(request, 'blog/posts/lavadora.html')

def jogo(request):
    return render(request, 'blog/posts/jogo.html')
