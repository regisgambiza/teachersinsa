from django.shortcuts import render
from mysite.models import Job
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    jobs = Job.objects.order_by('publication_date')[:10]

    return render(request, 'mysite/index.html', {'jobs':jobs})
