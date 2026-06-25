from django.shortcuts import render,get_object_or_404,redirect
from app1.models import Evaluation
# Create your views here.
def home(request):
    faculty=Evaluation.objects.all()
    return render(request,'home.html',{'fac':faculty})
def id(request,id):
    fac=get_object_or_404(Evaluation,id=id)
    return render(request,'id.html',{'fa':fac})
def add(request):
    if request.method=='POST':
        facname=request.POST['facname']
        subject=request.POST['subjectname']
        score=request.POST['score']
        email=request.POST['email']
        Evaluation.objects.create(fac_name=facname,subject=subject,score=score,email=email)
        return redirect('home')
    return render (request,'fac.html')
def edit(request,id):
    fac=get_object_or_404(Evaluation,id=id)
    if request.method=='POST':
        fac.fac_name=request.POST['facname']
        fac.subject=request.POST['subjectname']
        fac.score=request.POST['score']
        fac.email=request.POST['email']
        fac.save()
        return redirect('home')
        
    return render (request,'edit.html',{'fac':fac})
def delete(request,id):
    fac=get_object_or_404(Evaluation,id=id)
    fac.delete()
    return redirect('home')
