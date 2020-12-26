from django.http.response import HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import PasswordList
from .forms import PasswordForm
from django.contrib.auth.decorators import login_required
# Create your views here.

# FUnction to create data for the password safw


@login_required(login_url='login')
def create(request):
    
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            user = request.user
            password_name = form.cleaned_data['password_name']
            password_username = form.cleaned_data['password_username']
            password = form.cleaned_data['password']
            
            # p = PasswordList(user.id,password_name,password_username,password)
            p = PasswordList(int(user.id),password_name,password_username,password)
            p = PasswordList.objects.create(user_id = int(user.id),password_name = password_name,password_username = password_username,password = password)
            # request.user.PasswordList.add(p)
            print(user.id)
            print(id)
            print(user)
            p.save()

            saved = True
            return redirect('/create', {'form': form,'saved':saved})
    else:
        form = PasswordForm()
        # form.cleaned_data(password_name = password_name,)
    return render(request, 'create.html',{'form':form})

# function to display home page,and if user is authenticated, display snipets of password

@login_required(login_url='login')
def home(response):

    data = PasswordList.objects.filter(user = response.user)
    # user = get_object_or_404(PasswordList,pk = id)
    return render(response,'index.html',{'data':data})
@login_required(login_url='login')


# function to display full password list

def password_list(response):

    data = PasswordList.objects.filter(user = response.user)
    # user = get_object_or_404(PasswordList,pk = id)
    

    # Delete data from list

    # dynamically get id of data, pass to delete function n then execute
    return render(response,'password.html',{'data':data})



def delete_data(request):
    if request.method == 'GET':
        data = PasswordList.objects.filter(user = request.user)
        # to_delete = data.id
        
        for i in data:
            print(i.id)
            data_id = i.id
            to_delete = PasswordList.objects.get(pk=data_id)
        # print(data.id)
            to_delete.delete()
            return HttpResponseRedirect('/password_list')


# def update(request, todo_id):
#     todo = get_object_or_404(Todo, pk=todo_id)
#     isCompleted = request.POST.get('isCompleted', False)
#     if isCompleted == 'on':
#         isCompleted = True

#     todo.isCompleted = isCompleted

#     todo.save()
#     return redirect('todos:index')
