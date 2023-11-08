from django.shortcuts import render
from django.template import RequestContext

# Create your views here.
def google_auth(request):
  return render("accounts/google_login.html", context_instance=RequestContext(request))