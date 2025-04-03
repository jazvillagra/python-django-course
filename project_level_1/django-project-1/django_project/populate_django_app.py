import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()

from django_app.models import Topic, Webpage, AccessRecord
from faker import Faker
from random import randint, choice

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

# This function creates a new topic
def add_Topic():
    t = Topic.objects.get_or_create(top_name=choice(topics))[0]
    t.save()
    return t

# This function populates the database with fake data
def populate(n=5):
    for entry in range(n):
        # get the topic for the entry
        top = add_Topic()
        # create the fake data for that entry
        fake_url = fakegen.url()
        fake_name = fakegen.company()
        # create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
        # create the fake access record for that webpage
        fake_date = fakegen.date()
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]
        

# Print the number of records created
def print_records_created():
    print(f"Number of records created: {Webpage.objects.count()}")
    print(f"Number of records created: {AccessRecord.objects.count()}")

if __name__ == '__main__':
    print("Populating the database...Please Wait")
    populate(20)
    print("Populating Complete")
