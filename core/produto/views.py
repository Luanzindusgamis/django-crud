from django.shortcuts import render, redirect
from.models import Produto 

# Create your views here.
def home (request):
    produtos = Produto.objects.all()
    return render (request,'index.html',{'produtos':produtos})

def cadastro (request):
    return render (request,'cadastro.html',{})

def save(request):
    vdescricao = request.POST['descricao']
    vpreco= request.POST['preco']
    vquantidade= request.POST ['quantidade']
    Produto.objects.create(descricao=vdescricao,preco=vpreco,quantidade=vquantidade)
    produtos = Produto.objects.all()
    return render (request, 'index.html', {'produtos':produtos})

def atualiza(request,id):
    produto = Produto.objects.get(id=id)
    return render(request,'atualiza.html',{'produto':produto})

def update(request):
    id = request.POST['id']
    produto = Produto.objects.get(id=id)
    produto.descricao = request.POST['descricao']
    produto.preco = request.POST['preco']
    produto.quantidade = request.POST['quantidade']
    produto.save()
    return redirect(home)

def delete(request,id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect(home)