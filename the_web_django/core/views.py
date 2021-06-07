from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


def index(request):
    jinjohn = "https://scontent.fbkk13-2.fna.fbcdn.net/v/t1.6435-9/152032256_3917655728294455_602977999881134267_n.jpg?_nc_cat=107&ccb=1-3&_nc_sid=09cbfe&_nc_eui2=AeHDBMMAfmnSDJS_IwKD1PNGuIdqeA52fnK4h2p4DnZ-coDoNWWtvI-Okj5XOG44RxMI05C91qwwhaDU9fEYdF2b&_nc_ohc=ES14zuGvqtgAX_zRmuP&_nc_ht=scontent.fbkk13-2.fna&oh=3eb22f974781a29b939de17fee7feaab&oe=60E010F0"
    odds = "https://scontent.fbkk12-2.fna.fbcdn.net/v/t1.6435-9/43480475_304748833447892_1013295875910270976_n.jpg?_nc_cat=105&ccb=1-3&_nc_sid=09cbfe&_nc_eui2=AeH9btg4U4XxfvpuKoSGi-PFsOnBtPCt7y2w6cG08K3vLboFaWfI7QpqUMIcasIOXb3DrTObfIvLAqE_FtDBAIQ1&_nc_ohc=UuNGDKd1dvsAX_3cb4O&_nc_ht=scontent.fbkk12-2.fna&oh=2f45a3022bf58936a8a6ea69a91e713c&oe=60E24F9E"
    http = "<h1>Jin is here!</h1> \
            <h2>Jin the John</h2> \
            <img src=%s width='250' height='250'> \
            <div> \
              <p>I am a cadet software developer at \
              <img src=%s width='50' height='50'></p> \
            </div> \
            <p>It's been a long time since I last wrote HTML</p> \
            <p>I am very excited and READY to learn Django !!</p> \
           " % (jinjohn, odds)

    return HttpResponse(http)


class IndexView(View):
    def get(self, request):
        fullName = "Jinnawat Makwisai"
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
            }
        )
