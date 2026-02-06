from .models import Profile

def profile_context(request):
    if request.user.is_authenticated:
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            profile = Profile.objects.create(user=request.user)
        return {'user_profile': profile}
    return {'user_profile': None}
