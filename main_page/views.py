from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import FormView
from .models import CarInfo
from .forms import UserSignUpForm


def home(request):
    data = CarInfo.objects.all()
    context = {
        "data":data
    }
    return render(request, 'home.html', context)


class SignUpFormView(FormView):
    template_name = 'register.html'
    form_class = UserSignUpForm
    success_url = '/'

    usersignup = "active"
    status = False

    def get_context_data(self, **kwargs):
        context = super(SignUpFormView, self).get_context_data(**kwargs)
        context.update({'usersignup': self.usersignup})
        return context

    def form_valid(self, form):
        if form.is_valid():
            messages.success(self.request, 'Account Created Successfully !!')
            form.save()
        return super().form_valid(form)


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('home')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'title': 'log in'})


def Contact(request):
    from .models import Contact
    if request.method == "POST":
        cForm = Contact()
        cForm.name = request.POST.get("name")
        cForm.email = request.POST.get("email")
        cForm.comment = request.POST.get("comment")
        cForm.save()
        messages.success(request,"Contact form summited.!!")
        return redirect('/')
    return render(request, 'contactus.html')