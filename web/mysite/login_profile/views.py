from django.contrib.auth.models import User
from django.http import HttpResponse

def index(request):
    users = User.objects.all()
    for user in users:
        print user.userprofile.desc
    return HttpResponse(users)
