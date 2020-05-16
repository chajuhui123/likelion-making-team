from django.shortcuts import render
import random
# Create your views here.

def home(request):
    lion_member = ['민지','채원','지은','진우','희찬',
    '명환','지윤','바다','민정','예빈','은아','지원'
    ,'인아','재훈','주희']

    random.shuffle(lion_member)

    seul_team = lion_member[0:4]
    sea_team = lion_member[4:8]
    hey_team = lion_member[8:12]
    tea_team = lion_member[12:15]
    
    return render(request, 'home.html',{'seul':seul_team,'sea':sea_team,'hey':hey_team,'tea':tea_team})
