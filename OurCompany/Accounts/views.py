from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import UsersLogs,Notifications
from django.utils import timezone
# Create your views here.
@login_required
def home(request):
    if request.user.groups.filter(name="Employee").exists():
        return redirect('Home')
    elif request.user.groups.filter(name="Manager").exists():
        return redirect('Dashboard')
    
@login_required
def employee_home(request):
    UserLog = None
    try:
        UserLog = UsersLogs.objects.filter(is_logedout = False,user_id=request.user).first()
    except:
        UserLog=None
    if UserLog == None:
        new_UserLog = UsersLogs()
        new_UserLog.user_id = request.user
        new_UserLog.logedin_at = timezone.now()
        new_UserLog.save()
        UserLog = new_UserLog

    return render(request,'employee_home.html',{"CurrentLog":UserLog})

@login_required
def manager_home(request):
    # counters
    attendants = UsersLogs.objects.filter(is_logedout = False).count()
    leave_requests = UsersLogs.objects.filter(leave_request_at__isnull=False,is_logedout = False).count()
    context = {
        "attendants":attendants,
        "leave_requests":leave_requests
        }
    return render(request,'manager_home.html',context)

@login_required
def employees_requests(request):
    leave_req = UsersLogs.objects.filter(leave_request_at__isnull=False,allow_leave=False,is_logedout = False)
    not_read_notific = Notifications.objects.all().filter(is_readed = 0)
    for noti in not_read_notific:
        noti.is_readed = 1
        noti.save()
    return render(request,'employees_requests.html',{"leave_requests":leave_req})
