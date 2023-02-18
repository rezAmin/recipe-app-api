"""

 django command to wait for database to be available

"""
import time
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg20Error
from django.db.utils import OperationalError


class Command(BaseCommand):

    def handle(self, *args, **options):
        """ Entrypoint for command. """
        self.stdout.write('waiting for database ...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg20Error, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second ...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available.'))

