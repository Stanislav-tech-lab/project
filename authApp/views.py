from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.contrib.auth import get_user_model

User = get_user_model()

def auth_page(request):
    """
    One page for registration and login.
    mode query param controls visible form, default = register
    """
    mode = request.GET.get("mode", "register")

    # If POST, determine which form is submitted by hidden "mode" field
    if request.method == "POST":
        submitted_mode = request.POST.get("mode", "register")
        if submitted_mode == "register":
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()  # UserCreationForm handles password hashing
                login(request, user)
                messages.success(request, "Регистрация успешна. Вы вошли в систему.")
                return redirect("personal_account")
            else:
                # show register errors
                return render(request, "authApp/auth.html", {
                    "register_form": form,
                    "login_form": LoginForm(),
                    "mode": "register",
                })
        else:  # login
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password"]
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Вход успешен.")
                    return redirect("index")
                else:
                    form.add_error(None, "Неверный email или пароль")
            # show login with errors
            return render(request, "authApp/auth.html", {
                "register_form": RegisterForm(),
                "login_form": form,
                "mode": "login",
            })

    # GET — show empty forms
    return render(request, "authApp/auth.html", {
        "register_form": RegisterForm(),
        "login_form": LoginForm(),
        "mode": mode,
    })
