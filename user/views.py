from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View

from user.models import Profile


class ProfileView(ListView):
    model = Profile
    template_name = 'profile/profile.html'

