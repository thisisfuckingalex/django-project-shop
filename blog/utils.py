from django.shortcuts import render


class VisitsPostMixin:
    model = None
    template_name = None

    def get(self, request, pk_post):
        post = self.model.objects.filter(pk=pk_post)
        num_visits_post = request.session.get('num_visits_post', 0)
        request.session['num_visits_post'] = num_visits_post + 1
        return render(request, self.template_name, context={'post': post, 'num_visits_post': num_visits_post})