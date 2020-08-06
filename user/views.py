from django.views.generic import ListView

from user.models import Profile


class ProfileView(ListView):
    model = Profile
    template_name = 'profile/profile.html'

