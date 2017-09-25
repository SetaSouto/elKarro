from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views.generic import TemplateView


class Homeview(TemplateView):
    template_name = "users/login.html"

    def post(self, *args, **kwargs):
        username = self.request.POST['username']
        password = self.request.POST['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)

            print(user.has_perm("can_create_order"))
            if user.has_perm("can_create_order"):
                return redirect("users:create")
            if user.has_perm("can_deliver_order"):
                return redirect("users:create")
        return redirect("users:home")


class CreateOrderView(TemplateView):
    pass


class DeliverOrderView(TemplateView):
    pass
