from django.shortcuts import render,redirect,get_object_or_404
from playerapp.models import Player
# Create your views here.
def home(request):
    players=Player.objects.all()
    playname=request.GET.get('playname')
    if playname:
        players=Player.objects.filter(name=playname)
    return render(request,'home.html',{'play':players})
def welcome(request):
    return  render(request,'welcome.html')
def addplayer(request):
    if request.method=='POST':
        name=request.POST['name']
        innings=request.POST['innings']
        runs=request.POST['runs']
        Player.objects.create(name=name,testinnings=innings,runs=runs)
        return redirect('home')
    return render(request,'add.html')
def id(request,id):
    play=get_object_or_404(Player,id=id)
    return render(request,'id.html',{'play':play})
def edit(request,id):
    play=get_object_or_404(Player,id=id)
    if request.method=='POST':
        play.name=request.POST['name']
        play.testinnings=request.POST['innings']
        play.runs=request.POST['runs']
        play.save()
        return redirect('home')
    return render(request,'edit.html')
def delete(request,id):
    play=get_object_or_404(Player,id=id)
    play.delete()
    return redirect('home')