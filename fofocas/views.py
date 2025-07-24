from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Fofoca
from .forms import FofocaForm


def lista_fofocas(request):
    fofocas = Fofoca.objects.select_related('autor').order_by('-criado_em')
    return render(request, 'fofocas/lista.html', {'fofocas': fofocas})

@login_required
def nova_fofoca(request):
    form = FofocaForm(request.POST or None)
    if form.is_valid():
        fofoca = form.save(commit=False)
        fofoca.autor = request.user
        fofoca.save()
        return redirect('lista_fofocas')
    return render(request, 'fofocas/form.html', {'form': form})

def votar(request, fofoca_id, tipo):
    fofoca = get_object_or_404(Fofoca, id=fofoca_id)
    if tipo == 'confirmo':
        fofoca.votos_confirmo += 1
    elif tipo == 'mentira':
        fofoca.votos_mentira += 1
    fofoca.save()
    return redirect('lista_fofocas')



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})