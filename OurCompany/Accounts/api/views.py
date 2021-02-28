from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.models import User
from django.contrib.auth import logout
from Accounts.models import UsersLogs,Notifications
from .serializers import UsersLogsSerializer
from Accounts.api import serializers

@api_view(['GET'])
def api_get_all_logs(request):
    Userlogs = None
    try:
        Userlogs = UsersLogs.objects.filter(leave_request_at__isnull= False,is_logedout = False)
    except UsersLogs.DoesNotExist():
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UsersLogsSerializer(Userlogs,many=True)
        return Response(serializer.data)

@api_view(['POST'])
def leave_request(request,pk):
    #request_time = request.data['leave_request_at']
    
    UsersLog = None
    try:
        UsersLog = UsersLogs.objects.get(id=pk)
    except:
        UsersLog= None
    if UsersLog != None:
        UsersLog.leave_request_at = request.data['leave_request_at']
        UsersLog.save()
        return Response("request sent")
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def leave(request,pk):
    #request_time = request.data['leave_request_at']
    UsersLog = None
    try:
        UsersLog = UsersLogs.objects.get(id=pk)
    except:
        UsersLog= None
    if UsersLog != None:
        UsersLog.logedout_at = request.data['logedout_at']
        UsersLog.is_logedout = 1
        UsersLog.save()
        logout(request)
        return Response("user logged out")
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def approve_request(request,pk):
    UsersLog = None
    try:
        UsersLog = UsersLogs.objects.get(id=pk)
    except:
        UsersLog= None
    if UsersLog != None:
        UsersLog.allow_leave = 1
        UsersLog.save()
        return Response("user approverd to leave")
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def cancel_request(request,pk):
    UsersLog = None
    try:
        UsersLog = UsersLogs.objects.get(id=pk)
    except:
        UsersLog= None
    if UsersLog != None:
        UsersLog.leave_request_at = None
        UsersLog.save()
        return Response("user not permitted to leave")
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_UserLog(request,pk):
    UsersLog = None
    try:
        UsersLog = UsersLogs.objects.get(id=pk)
    except:
        UsersLog= None
    if UsersLog != None:
        UsersLog.delete()
        return Response("Log successfully deleted !!")
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_notification(request):
    new_Noti = Notifications()
    new_Noti.n_from = request.data['n_from']
    new_Noti.message = request.data['message']
    new_Noti.created_at = request.data['at']
    new_Noti.save()
    return Response("notification added")

@api_view(['GET'])
def read_noti(request,noti_id):
    Noti = None
    try:
        Noti = Notifications.objects.get(id=noti_id)
    except:
        Noti= None
    if Noti != None:
        Noti.is_readed = 1
        Noti.save()
        return Response("Noti has been read successfully !!")
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

# serializer = UsersLogsSerializer(instance = UsersLog,data=request.data)
#         if serializer.is_valid():
#             serializer.save()