from .constants import JINJOHN_IMG, ODDS_IMG

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import Profile, Subscriber
from .forms import SubscriberForm
from core.serializers import SubscriberSerializer, ProfileSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets


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


class SubscriberAPIView(APIView):
    def get(self, request):
        subscriber = Subscriber.objects.all()
        serializer = SubscriberSerializer(subscriber, many=True)

        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
