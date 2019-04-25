from django.shortcuts import render
from django.views.generic import TemplateView
from rotavid.models import *


# Create your views here.

def IndexPage(request):
	if request.method == "POST":
		
		Ano=request.POST['Ano']
		Sname=request.POST['Sname']
		Sphoto=request.FILES['mycover1']


		Fname=request.POST['Fname']
		Fphoto=request.FILES['mycover2']

		Mname=request.POST['Mname']
		Mphoto=request.FILES['mycover3']

		School=request.POST['School']
		Grade=request.POST['Grade']
		PYmarks=request.FILES['mycover4']

		PPYmarks=request.FILES['mycover5']
		Marks=request.POST['Marks']
		Incomecert=request.FILES['mycover6']

		Foccup=request.POST['Foccup']
		Moccup=request.POST['Moccup']
		Sfee=request.POST['Sfee']		
		Scholar=request.POST['Scholar']
		new_student=Student.objects.create(Ano=Ano,Sname=Sname,Sphoto=Sphoto,Fname=Fname,
			Fphoto=Fphoto,Mname=Mname,Mphoto=Mphoto,
			School=School,Grade=Grade,PYmarks=PYmarks,
			PPYmarks=PPYmarks,Marks=Marks,Incomecert=Incomecert,
			Foccup=Foccup,Moccup=Moccup,Sfee=Sfee,Scholar=Scholar)

		print(new_student)
	return render(request, "index.html")

def details(request):
	students=Student.objects.all()
	
	return render(request,"data.html",{"students":students})

def details_student(request,id):
	appno=Student.objects.get(pk=id)
	print(appno)


	return render(request,"details_student.html",{"appno":appno})



