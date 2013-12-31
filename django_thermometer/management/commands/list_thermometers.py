from django.core.management.base import BaseCommand, CommandError
from django_thermostat.rules import evaluate
from time import localtime, strftime


class Command(BaseCommand):
    args = ''
    help = 'Read temperature from the DS18B20 termometers'

    def handle(self, *args, **options):
        pass
