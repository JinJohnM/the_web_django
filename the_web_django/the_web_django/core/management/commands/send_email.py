from django.core.management.base import BaseCommand, CommandError
from django.core.mail import send_mail

from core.models import Subscriber


class Command(BaseCommand):
    help = 'sends email to all subscriber'

    def handle(self, *args, **options):
        try:
            subscribers = Subscriber.objects.all()
            counter = 0
            for subscriber in subscribers:
                counter += 1
                print("Recipient: ", counter)
                send_mail(
                    "This is A Subject",
                    "I have a message for you!",
                    None,
                    [subscriber.email],
                )
        except Exception as e:
            print(e)
            raise CommandError("Error!")
