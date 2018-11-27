from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def index(request):
    if request.user.is_authenticated:
        if request.user.is_doctor:
            return redirect('doctor:profile')
        else:
            return redirect('patient:profile')
    return render(request, 'home/index.html')