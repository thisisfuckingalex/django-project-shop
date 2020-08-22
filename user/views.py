from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView

from user.models import Profile


class ProfileView(ListView):
    model = Profile
    template_name = 'profile/profile.html'


# class ProfileUpdate(UpdateView):
#     model = Profile
#     template_name = 'profile/profile_update.html'
#     pk_url_kwarg = 'pk_profile'
#     success_url = ''
#     fields = ['first_name', 'last_name', 'address']
#
#     def form_valid(self, form, pk_profile=False):
#         if pk_profile is not False:
#             form = form(pk_profile=pk_profile)
#             form.user = self.request.profile.user
#             form.save()



