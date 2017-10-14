from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

# BEGIN_OF_CODE_GENERATION

# END_OF_CODE_GENERATION


@login_required()
def home_page(request):
    template_name = 'app/home_page.html'
    return render(request, template_name, {'user': request.user})