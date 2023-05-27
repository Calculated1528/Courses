from .models import UserInfo

def GetUserInfo(request):
    current_user = request.user
    if current_user.is_authenticated:
        userInfo = UserInfo.objects.get(user = current_user)
        return {'userInfo': userInfo}
    else:
        return {'userInfo': UserInfo}