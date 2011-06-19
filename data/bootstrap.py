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
    reader = csv.DictReader(open('data/programs.csv'))
    for program in reader:
        # the stars data is seriously broken
        # there's all kinds of insanity and spammity in there
        # trying to filter some basically usable stuff...
        if ( (program['program'].strip() != '') and
             (program['address'].strip() != '') and
             (program['ages'].find('18') > -1)):
            
            name = program['program'].strip()
            agency = program['agency'].strip()
            address = program['address'].strip()
            city = program['city'].strip()
            state = program['state'].strip()
            zip = program['zip'].strip()
            district = program['district'].strip()
            phone = program['phone'].strip()
            fax = program['fax'].strip()
            tdd = program['tdd'].strip()
            email = program['email'].strip()
            web = program['web'].strip()

            address, _ = Address.objects.get_or_create(
                    street1 = address,
                    city = city,
                    state = state,
                    zipcode = zip)

            contact, _ = Contact.objects.get_or_create(
                    phone = phone,
                    fax = fax,
                    tdd = tdd,
                    email = email,
                    web = web)

            existing_orgs = Organization.objects.filter(name=name)
            if existing_orgs:
                organization = existing_orgs[0]
            else:
                organization, _ = Organization.objects.get_or_create(
                        name = name,
                        headoffice = address)

            organization.contacts.add(contact)
            organization.save()




