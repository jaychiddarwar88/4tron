from django.shortcuts import render
from django.http import HttpResponse
from .models import querydetail, visitcounter
from .emailhandler import sendmail


# Create your views here.

def index(request):
    counter = visitcounter.objects.get(pk = 1)
    visit = counter.modelcount + 1
    visitcounter.objects.filter(pk = 1).update(modelcount = visit)
    visit = visitcounter.objects.get(pk = 1).modelcount
    print(visit)
    return render(request, "tron4/index.html", {"totalvisit" : visit})


def ajaxquery(request):
    uname = request.POST['qname']
    uphoneno = request.POST['qphoneno']
    uemail = request.POST['qemail']
    umsg = request.POST['qmsg']
    querydetail.objects.create(name = uname, phoneno = uphoneno, email = uemail, msg = umsg)
    sendmail(uemail, "here is query from 4tron studios from : " + uname, umsg + "\n\n\n\n\n\n\n\n\nUser's Phone Number is : " + uphoneno)
    return HttpResponse("success")