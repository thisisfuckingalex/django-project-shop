from django.shortcuts import render


class OrderMixin:
    model = None
    template_name = None

    def get(self, request, ):
        orders = self.model.objects.filter()
        return render(request, self.template_name, context={'orders': orders})