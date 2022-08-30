from django.shortcuts import render
from myfiles.models import Teacher,Fan
# Create your views here.
def home(malumot):
    return render(malumot,'asosiy.html')

def oqituvchilar(malumot):
    if 'idd' in malumot.POST:
        ismi = malumot.POST.get('ism')
        familya = malumot.POST.get('fam')
        yosh = malumot.POST.get('age')
        sana = malumot.POST.get('kun')
        fan_id = malumot.POST.get('fan')
        fan = Fan.objects.get(id=fan_id)
        id_raqam = malumot.POST.get('idd')
        Teacher(id=id_raqam,ism=ismi, fam=familya, yosh=yosh, sana=sana, fan=fan).save()
    elif malumot.method =="POST":
        ismi = malumot.POST.get('ism')
        familya = malumot.POST.get('fam')
        yosh = malumot.POST.get('age')
        sana = malumot.POST.get('kun')
        fan_id = malumot.POST.get('fan')
        fan = Fan.objects.get(id=fan_id)
        Teacher(ism=ismi,fam=familya,yosh=yosh,sana=sana,fan=fan).save()

    teachers = Teacher.objects.all().order_by('id')
    return render(malumot,'teachers.html',{'techs':teachers})


def adding(malumot):
    fanlar = Fan.objects.all()
    return render(malumot,'add_teacher.html',{'fans':fanlar})

def ochirish(malumot,s):
    oqituvchi  = Teacher.objects.get(id=s).delete()
    teachers = Teacher.objects.all()
    return render(malumot,'teachers.html',{'techs':teachers})


def update_t(malumot,id):
    oqituvchi = Teacher.objects.get(id=id)
    fanlar = Fan.objects.all()
    return render(malumot,'update_teacher.html',{"teach":oqituvchi,'fans':fanlar})








"""
CRUD
C --- CREATE --- YARATISH
R --- READ   --- O'QIMOQ
A --- ADD    --- QO'SHISH
U --- UPDATE --- O'ZGARTIRMOQ
D --- DELETE --- O'CHIRMOQ




"""