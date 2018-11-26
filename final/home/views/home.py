from django.shortcuts import redirect, render


def index(request):
    if request.user.is_authenticated:
        if request.user.is_doctor:
            return redirect('doctor:profile')
        else:
            return redirect('patient:profile')
    return render(request, 'home/')