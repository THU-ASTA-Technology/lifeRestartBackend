from django.http import HttpResponse
from database.models import Achievement

 
# 接收请求数据
def upload(request):
    if (request.GET and request.GET.get('username') and request.GET.get('achievementName')):
        Achievement(username = request.GET.get('username'), achievement = request.GET.get('achievementName')).save()
        return HttpResponse("Successful", status = 200)
    else:
        return HttpResponse("Data missing", status = 400)

def leaderboard(request):
    list = Achievement.objects.all()
    map = {}
    for a in list:
        if not a.username in map:
            map[a.username] = []
        if not a.achievement in map[a.username]:
            map[a.username].append(a.achievement)
    board = [(user, len(map[user]), map[user]) for user in map]
    board = sorted(board, key = lambda kv:(kv[1], kv[0]))
    print(board)
    return HttpResponse("</br>".join([" ".join([str(x) for x in item]) for item in board]), status = 200)