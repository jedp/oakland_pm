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

            print "Imported school:", school
                        
def bootstrap_organizations():
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
                        headoffice = address,
                        contact=contact)

            print "Imported org:", organization
                    
def bootstrap_categories():
    for category in [
            'Art',
            'Music',
            'Dance',
            'Sports',
            'Cooking',
            'Theater',
            'Photography',
            'Film',
            'Woodworking',
            'Metalsmithing',
            'Math', 
            'Science', 
            'Literature',
            'Writing',
            ]:
        print "Instaling category:", category
        Category.objects.get_or_create(name=category)

def bootstrap_tags():

    for tag in ['animals', 'architecture', 'art', 'asia', 'australia',
            'autumn', 'baby', 'band', 'barcelona', 'beach', 'berlin', 'bike',
            'bird', 'birds', 'birthday', 'black', 'blackandwhite', 'blue',
            'bw', 'california', 'canada', 'canon', 'car', 'cat', 'chicago',
            'china', 'christmas', 'church', 'city', 'clouds', 'color',
            'concert', 'dance', 'day', 'de', 'dog', 'england', 'europe',
            'fall', 'family', 'fashion', 'festival', 'film', 'florida',
            'flower', 'flowers', 'food', 'football', 'france', 'friends',
            'fun', 'garden', 'geotagged', 'germany', 'girl', 'graffiti',
            'green', 'halloween', 'hawaii', 'holiday', 'house', 'india',
            'instagramapp', 'iphone', 'iphoneography', 'island', 'italia',
            'italy', 'japan', 'kids', 'la', 'lake', 'landscape', 'light',
            'live', 'london', 'love', 'macro', 'me', 'mexico', 'model',
            'mountain', 'museum', 'music', 'nature', 'new', 'newyork',
            'newyorkcity', 'night', 'nikon', 'nyc', 'ocean', 'old', 'paris',
            'park', 'party', 'people', 'photo', 'photography', 'photos',
            'portrait', 'raw', 'red', 'river', 'rock', 'san', 'sanfrancisco',
            'scotland', 'sea', 'seattle', 'show', 'sky', 'snow', 'spain',
            'spring', 'square', 'squareformat', 'street', 'summer', 'sun',
            'sunset', 'taiwan', 'texas', 'thailand', 'tokyo', 'toronto',
            'tour', 'travel', 'tree', 'trees', 'trip', 'uk', 'urban', 'usa',
            'vacation', 'vintage', 'washington', 'water', 'wedding', 'white',
            'winter', 'yellow', 'zoo']:
        print "Installing tag:", tag
        Tag.objects.get_or_create(name=tag)

def bootstrap_programs():
    import re
    import random

    program_block = re.compile("""
        ^
        ([A-Z].*?[A-Z]$)    # All-caps heading, w/ punct maybe
        (?:[\n]*)
        (\w.*?$)            # description
        (?:[\n]*)
        (?:.*?:\s+)
        (.*?)               # Address
        \s+Age.*            # ignore age
        (?:[\n]+)
        Strategy.*?$        # ignore stragety type
        (?:[\s]*)""",
        re.MULTILINE | re.VERBOSE)

    programs = open('data/ofcy.txt').read()
    all_categories = [o.name for o in Category.objects.all()]
    all_tags = [o.name for o in Tag.objects.all()]

    for match in program_block.finditer(programs):
        title, summary, street = match.groups()

        # this won't get words in parens, but whatever
        title = ' '.join(
                map( lambda word: word.capitalize(), 
                    title.split()))

        address, _ = Address.objects.get_or_create(
                street1 = street ) 
        program, _ = Program.objects.get_or_create(
                name = title,
                summary = summary,
                address = address)

        # add two categories and five tags at random
        for i in range(2):
            name = random.choice(all_categories)
            program.categories.add(
                    Category.objects.get(name=name))
        
        for i in range(5):
            name = random.choice(all_tags)
            program.tags.add(
                    Tag.objects.get(name=name))

        print "Imported and tagged program:",  title

def bootstrap_events():
    """
    assign some dates to thing
    """
    import datetime
    import random
    # let's have each event occur once between 3 and 6 pm, 
    # some day in the next month, and then recur for the next 1 to 8 weeks

    now = datetime.datetime.now().replace(minute=0, second=0)

    for program in Program.objects.all():
        start_hour = random.randint(15, 18)
        the_date = now.replace(hour=start_hour) + datetime.timedelta(random.randint(0, 31))
        duration = random.randint(1,6) * 30
        next_week = datetime.timedelta(7)

        program.events.add(EventDate.objects.create(
            date=the_date, 
            duration_mins = duration))

        for next_occur in range(random.randint(1,8)):
            the_date += next_week
            program.events.add(EventDate.objects.create(
                date = the_date,
                duration_mins = duration))

        print "Scheduled", program.events.count(), "events for", program

def main():
    bootstrap_schools()
    bootstrap_organizations()
    bootstrap_categories()
    bootstrap_tags()
    bootstrap_programs()
    bootstrap_events()
