from .models import Notifications

def add_notification_to_context(request):
    Notifs = Notifications.objects.all().order_by('-created_at')
    not_read = Notifications.objects.filter(is_readed = 0).count()
    context = {
        "notifs": Notifs,
        "not_read": not_read
    }
    return context