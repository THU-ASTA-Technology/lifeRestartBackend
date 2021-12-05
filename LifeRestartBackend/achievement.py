from django.http import HttpResponse
from database.models import Achievement

 
# 接收请求数据
def upload(request):
    if (request.GET and request.GET.get('username') and request.GET.get('achievementName')):
        Achievement(username = request.GET.get('username'), achievement = request.GET.get('achievementName')).save()
        return HttpResponse("Successful", status = 200)
    else:
        return HttpResponse("Data missing", status = 400)