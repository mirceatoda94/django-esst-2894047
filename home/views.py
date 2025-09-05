from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime

def home_view(request):
    today = datetime.today()
    return render(request, "home/welcome.html", {"today": today})

@login_required(login_url="/admin/login/")
def authorized_view(request):
    return render(request, "home/authorized.html", {})
