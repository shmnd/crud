from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Students
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.



class StudentsList(ListView):
    model=Students

# class StudentsView(DetailView):
#     model=Students
    

class StudentCreate(CreateView):
    model=Students
    fields=['sno','sname','sage','splace','smajor']
    success_url=reverse_lazy('stud_list')

class StudentUpdate(UpdateView):
    model=Students
    fields=['sno','sname','sage','splace','smajor']
    success_url=reverse_lazy('stud_list')

class StudentsDelete(DeleteView):
    model=Students 
    success_url=reverse_lazy('stud_list')







# def show(request):

#     allstud=Students.objects.all()
#     mydict={
#         'info':allstud
#     }
#     return render(request,'app1/app1.html',mydict)

# def add(request):
#     return render(request,'app1/add.html')


# def addrec(request):
#     if request.method=='POST':
#         w=request.POST['sno']
#         x=request.POST['sname']
#         y=request.POST['sage']
#         z=request.POST['splace']
#         a=request.POST['smajor']
#         if w and x and y and z and a:
#             stu=Students.objects.create(sno=w,sname=x,sage=y,splace=z,smajor=a)
#             stu.save()
#             return redirect('show')
#         else:
#             return HttpResponse(f'Invalid operation')
#     else:
#         return HttpResponse('this view only accept post request')
    
# def delrec(request,id):
#     stu=Students.objects.get(id=id)
#     print(stu,'iddddddddddd')
#     stu.delete()
#     return redirect('show')
    

# def update(request,id):
#     stu=Students.objects.get(id=id)
#     return render(request,'app1/upd.html',{'stu':stu})


# def uprec(request,id):
#     w=request.POST['no']
#     x=request.POST['name']
#     y=request.POST['age']
#     z=request.POST['place']
#     a=request.POST['major']

#     stu=Students.objects.get(id=id)
#     stu.sno=w
#     stu.sname=x
#     stu.sage=y
#     stu.splace=z
#     stu.smajor=a
#     stu.save()
#     return redirect('show')

