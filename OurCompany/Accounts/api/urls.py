from django.urls import path
from .views import *
app_name = 'Accounts'
urlpatterns = [
    path('',api_get_all_logs,name="all_logs"),
    path('leave_request/<str:pk>/',leave_request,name="leave_request"),
    path('leave/<str:pk>/',leave,name="leave"),
    path('approve_request/<str:pk>/',approve_request,name="approve_request"),
    path('cancel_request/<str:pk>/',cancel_request,name="cancel_request"),
    path('push_noti/',add_notification,name="push_noti"),
    path('read_noti/<str:noti_id>/',read_noti,name="read_noti"),
    path('delete_log/<str:pk>/',delete_UserLog,name="delete_log"),
]