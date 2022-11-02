from django.shortcuts import render
from stuinfo import forms

# Create your views here.

def student_input(request):
    sent=False
    form=forms.studentform()
    if request.method=='POST':
        form=forms.studentform(request.POST)
        if form.is_valid():
            print('form validation success and proiting data')
            print('name:',form.cleaned_data['name'])
            print('marks:',form.cleaned_data['marks'])
            sent=True
        form=forms.studentform()    
    return render(request,'stuinfo/input.html',{'form':form,'sent':sent})        

