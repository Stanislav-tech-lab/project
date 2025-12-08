from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def personal_account(request):
    user = request.user

    # Подключаем шаблон в зависимости от роли
    if user.role == "client":
        template = "personalAccount/client_info.html"
    elif user.role == "doctor":
        template = "personalAccount/doctor.html"
    elif user.role == "storekeeper":
        template = "personalAccount/storekeeper.html"
    elif user.role == "zavOtdel":
        template = "personalAccount/zavOtdel.html"
    elif user.role == "Registrat":
        template = "personalAccount/Registrat.html"
    elif user.role == "zavOtdel":
        template = "personalAccount/zavOtdel.html"
    elif user.role == "labor":
        template = "personalAccount/labor.html"
    elif user.role == "zavDiagn":
        template = "personalAccount/zavDiagn.html"
    elif user.role == "ZavIzgot":
        template = "personalAccount/ZavIzgot.html"                
    else:
        template = "personalAccount/owner.html"

    return render(request, template)



# Create your views here.