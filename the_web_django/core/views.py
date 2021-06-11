from .constants import JINJOHN_IMG, ODDS_IMG
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import Profile, Subscriber
from .forms import SubscriberForm


def index(request):
    http = (
        "<h1>Jin is here!</h1> \
            <h2>Jin the John</h2> \
            <img src=%s width='250' height='250'> \
            <div> \
              <p>I am a cadet software developer at \
              <img src=%s width='50' height='50'></p> \
            </div> \
            <p>It's been a long time since I last wrote HTML</p> \
            <p>I am very excited and READY to learn Django !!</p> \
           "
        % (JINJOHN_IMG, ODDS_IMG)
    )

    return HttpResponse(http)


class IndexView(View):
    def get(self, request):
        profile = Profile.objects.get(id=1)

        form = SubscriberForm()

        fullName = profile.name
        name = "Jin"
        workplace = "ODDS"
        jobTitle = "cadet software developer"

        return render(
            request,
            "index.html",
            {
                "fullName": fullName,
                "name": name,
                "workplace": workplace,
                "jobTitle": jobTitle,
                "form": form,
            },
        )

    def post(self, request):
        profile = Profile.objects.get(id=1)

        form = SubscriberForm(request.POST)
        if form.is_valid():
            cleanedData = form.cleaned_data.get("email")
            Subscriber.objects.create(email=cleanedData)

        fullName = profile.name
        name = "Jin"
        workplace = "ODDS"
        jobTitle = "cadet software developer"

        return render(
            request,
            "index.html",
            {
                "fullName": fullName,
                "name": name,
                "workplace": workplace,
                "jobTitle": jobTitle,
                "form": form,
            },
        )
