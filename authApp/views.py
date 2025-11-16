from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from .forms import RegisterForm, LoginForm

User = get_user_model()

def auth_page(request):
    mode = request.GET.get("mode", "register")  # по умолчанию регистрация

    if request.method == "POST":
        if request.POST.get("mode") == "register":
            form = RegisterForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password"]
                repeat = form.cleaned_data["repeat_password"]

                if password != repeat:
                    form.add_error("repeat_password", "Пароли не совпадают")
                else:
                    user = User.objects.create_user(email=email, password=password)
                    user.save()
                    login(request, user)
                    return redirect("index")
        else:
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password"]

                user = authenticate(request, email=email, password=password)

                if user:
                    login(request, user)
                    return redirect("index")
                else:
                    form.add_error(None, "Неверный email или пароль")

    # GET запрос → показываем пустые формы
    return render(request, "authApp/auth.html", {
        "register_form": RegisterForm(),
        "login_form": LoginForm(),
        "mode": mode,
    })
