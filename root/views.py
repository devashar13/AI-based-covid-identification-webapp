from django.shortcuts import render,redirect
from .detect import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here. 
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created !')
            return redirect('login')
    else:
        form =UserCreationForm()
    return render(request, 'root/register.html', {'form': form})
@login_required
def home_view(request): 
    
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES) 
        image=Predict()
        if form.is_valid(): 
            form.save()
            x_ray_img=request.FILES['x_ray_img'] 
            result = image.predict(x_ray_img)

            return render(request,'root/result.html',{'result':result})
            # return redirect('result') 
    else: 
        form = UserForm() 
        return render(request, 'root/index.html', {'form' : form}) 
  
  
# def success(request): 
#     result=detect()
#     return HttpResponse('successfully uploaded')

