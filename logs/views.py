from django.shortcuts import render, redirect, get_object_or_404
from .models import LogsCorrida
from django.contrib.auth.decorators import login_required

@login_required
def lista_logs(request):
    logs = LogsCorrida.objects.filter(user=request.user).order_by('-date')
    return render(request, 'lista_logs.html', {'logs': logs})

@login_required
def adicionar_log(request):
    if request.method == 'POST':
       distancia = request.POST['distancia']
       tempo = request.POST['tempo']
       ritmo = request.POST['ritmo']
       observacoes = request.POST.get('observacoes', '')
       LogsCorrida.objects.create(
            user=request.user,
            distancia=distancia,
            tempo=tempo,
            ritmo=ritmo,
            observacoes=observacoes
        )
       return redirect('lista_logs')
    return render(request, 'adicionar_log.html')

def editar_log(request, id):
    log = get_object_or_404(LogsCorrida, id=id)
    if request.method == 'POST':
        # Atualiza os campos do log com os dados enviados no formulário
        log.distancia = request.POST['distancia']
        log.tempo = request.POST['tempo']
        log.ritmo = request.POST['ritmo']
        log.observacoes = request.POST.get('observacoes', '')
        log.save()

        return redirect('lista_logs')  # Redireciona para a lista de logs após a edição

    # Se for um GET, renderiza o formulário de edição com os dados do log
    return render(request, 'editar_log.html', {'log': log})

def deletar_log(request, id):
    log = get_object_or_404(LogsCorrida, id=id)
    if request.method == 'POST':
        log.delete()
        return redirect('lista_logs')
    return render(request, 'deletar_log.html', {'log': log})

