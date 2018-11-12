from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import getpass


class Command(BaseCommand):

	help = 'Create Superuser users'

	def handle(self, *args, **options):
		username = input('Enter your name: ')
		password = getpass.getpass('Enter your password: ')
		password2 = getpass.getpass('Enter your password again: ')
		while password != password2:
			password2 = getpass.getpass('Passwords do not match, enter your password again: ')
		User.objects.create_superuser(username=username, email='', password=password)	
		print('Superuser created successfully')

