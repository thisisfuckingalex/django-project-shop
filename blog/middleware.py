from django.contrib.auth.models import User
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class FirstMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_superuser:
            print('hi stuff')
        elif request.user.is_anonymous:
            print('HI привет двачевский анон ^_^')
        else:
            print('HI ORDINARY USER')


class SecondMiddleware(MiddlewareMixin):
    def __call__(self, request):
        print('SecondMiddleware 1')
        response = self.get_response(request)
        print('SecondMiddleware 2')
        return response
