from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='login_page')
def first_page(request):

    context = {

               }
    return render(request, 'learners_app/first_page.html', context)