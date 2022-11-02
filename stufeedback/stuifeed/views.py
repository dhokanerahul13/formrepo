import re
from django import forms
from django.shortcuts import render
from.import forms
# Create your views here.

def feedbackview(request):
    form=forms.feedbackform()
    if request.method=='POST':
        form=forms.feedbackform(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            rollno=form.cleaned_data['rollno']
            email=form.cleaned_data['email']
            feedback=form.cleaned_data['feedback']
    return render(request,'stuifeed/feedback.html',{'form':form})            