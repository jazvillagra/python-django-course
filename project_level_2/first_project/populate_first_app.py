import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
django.setup()

import random
from first_app.models import Users
from faker import Faker

fakegen = Faker()

def populate(n=5):
    for entry in range(n):
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        user = Users.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]
        user.save()
        print(f"Created user: {user.first_name} {user.last_name} with email: {user.email}")

if __name__ == '__main__':
    print("Populating the database with fake users...")
    populate(10)
    print("Database populated successfully!")
# This script populates the database with fake user data using the Faker library.
# It creates 10 users with random first names, last names, and email addresses.