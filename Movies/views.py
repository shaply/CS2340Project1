from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def create_review(request):
    

    return ""

@login_required
def update_review(request):
    return ""

@login_required
def delete_review(request):
    return ""