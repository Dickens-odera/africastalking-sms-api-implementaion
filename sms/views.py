from django.shortcuts import render, redirect
from django.http import HttpResponse
from sms.forms import RecipientsForm
from sms.models import Recipients
# Create your views here.
import africastalking
def index(request):
    api_key = "960446c716255923f44fbe03cb86709bbd0baea29e7e5e1c835601f778b42f2b"
    recipients = Recipients.objects.all()
    form = RecipientsForm(request.POST or None)
    template = 'sms/index.html'
    context = {"form":form, "recipients":recipients}
    if form.is_valid():
        form.save()
        return redirect("index-page")
    return render(request, template, context)


    

