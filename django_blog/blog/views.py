from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ProfileUpdateForm

@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, "blog/profile.html", {"form": form})
