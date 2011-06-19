import csv
from core.models import *

def bootstrap_schools():
    reader = csv.DictReader(open('data/schools.csv'))
    for school in reader:
        if school['TYPE'] == 'High':
            address = school['ADDRESS']
            phone = school['PHONE_1']

            # School names come in screaming in all caps.
            # Could it look more institutional and asinine?
            # Normalize caps.
            name = ' '.join(
                    map( lambda word: word.capitalize(), 
                        school['SCHOOL'].split()))

            contact, _ = Contact.objects.get_or_create(phone=phone)

            address, _ = Address.objects.get_or_create(
                    street1 = address,
                    city = 'Oakland',
                    state = 'CA')

            school, _ = School.objects.get_or_create(
                    name=name,
                    contact=contact,
                    address=address)

            print "Imported:", school
                        
def bootstrap_programs():

