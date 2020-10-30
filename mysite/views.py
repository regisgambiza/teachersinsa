from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from mysite.models import Job


# Create your views here.
def index(request):
    jobs = Job.objects.order_by('publication_date')[:10]  # returns 7 most recently posted jobs

    return render(request, 'mysite/index.html', {'jobs': jobs})


def search(request):
    q = request.GET.get('q', None)
    jobs = ''
    if q is None or q is "":
        jobs = Job.objects.all()
    elif q is not None:
        jobs = Job.objects.filter(title__icontains=q)

    return render(request, 'mysite/jobs.html', {'jobs': jobs})


def job_details(request, slug=None):
    job = get_object_or_404(Job, slug=slug)
    context = {'job': job}
    return render(request, 'mysite/job_details.html', context)
