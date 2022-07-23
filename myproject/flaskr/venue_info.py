from faker import Faker
import random
from random import randint, randrange
from faker_web import WebProvider
import re
from faker_e164.providers import E164Provider
import phonenumbers
fake = Faker(locale='en_US')

#-------------------------------------------------------#
# turn the fake numbers into xxx-xxx-xxxx format
#ex: +1-100-695-4529x5551, 744.048.4866x174, 001-622-733-1574, (813)376-9178
#-------------------------------------------------------#



final_result = ''
def check_number(number1):
    
    number = ''
    # number1 = fake.phone_number()
    # print(number1)
    # # print(number)
    new_number = phonenumbers.parse(number1, 'US')
    area_number = phonenumbers.format_number(new_number, phonenumbers.PhoneNumberFormat.NATIONAL)
    # print(area_number)
    number_list = str(area_number).split(' ')
    # print(number_list)
    if len(number_list) > 1:
        # print('number1')
        # print(number_list[0])
        # print(number_list[1])
        first_two = ''.join(number_list[:2])
        # print(first_two)
        number = ''.join(e for e in first_two if e.isnumeric())
        # print(number)
        final_result=(number_format(number))
    else: 
        # print('number2')
        number = number_list[0]
        final_result=(number_format(number))

    return final_result
    
   
def number_format(number):

    first_transformation=''
    if len(number) >10 :
        new = format(int(number[:-1]), ",").replace(",", "-") + number[-1]
        # print(new)
        new_number = re.findall('[0-9]{3}\-[0-9]{3}\-[0-9]{3}', new)[0]
        #print(new_number)
        first_transformation=new_number
    elif len(number) == 10 or number.startswith('00'):
        first_transformation=format(int(number[:-1]), ",").replace(',', '-')+number[-1]
        #   print(format(int(number[:-1]), ",").replace(',', '-')+number[-1])
    elif len(number) == 10 and number.startswith('0'):
        first_transformation = number[0]+format(int(number[:-1]), ",").replace(',', '-')+number[-1]
        #print(number[0]+format(int(number[:-1]), ",").replace(',', '-')+number[-1])
    return first_transformation
    



number1 = fake.phone_number()
print(check_number(number1))
# number_format('0014746603790')

'0010486761709'
#['(467)', '766-3257']

  
# print(len(number))
# check_number('0015987465970')
# check_number('(221) 842-4315)')
# check_number('0403324447')



# fake.add_provider(E164Provider)
# from faker_music import MusicProvider

# from random import randint, randrange
#-----------------#
#Faking 20 cases for testing

#-----------------#

# restaurant_list = ['Dubious Clams Brewing Company', 'The Drunken', "Sammie's",'un·cooked', 'Water Pig', 'Fry the music', 'Egg Slut', 'Call Your Mother', 'Foulmouthed Brewing', 'Meet Classical',
# 'The Catbird Seat', 'Hot Chix – Boston', "Obed and Isaac's", 'Fat Baby', 'Plan B Running', 'Bun Huggers Old Fashion',  
# 'Spanked Puppy', 'Holy Accustic', 'Tandem Coffee + Bakery', 
# 'Mr. & Mrs. Bun', 'Phlavz']

# #wont use from faker_music based on the website prerequisite
# genre_choices=[
#             ('Alternative'), ('Blues'), ('Classical'), ('Country'), ('Electronic'), ('Folk'), ('Funk'), ('Hip-Hop'),
#             ('Heavy Metal'), ('Instrumental'), ('Jazz'), ('Musical Theatre'), ('Pop'), ('Punk'), ('R&B'),('Reggae'),
#             ('Rock n Roll'), ('Soul'), ('Other')
#         ]

# seeking_description = ['Talented artist who is willing to perform and share music', 'No expereinced is not problem; we are looking for musicians who has passion, even just new to the field', 'its a great and friendly place for performers']
# # print(type(choices[1]))
#----------------------------------
# new = fake.msisdn()
# def phone_number_format():
#     for i in range(10):
#         new = fake.phone_number()
#     # new_format = ''.join(e for e in new if e.isnumeric())
#     # if len(new_format)>10:
#         new_regex = re.sub('[^0-9]+', '', new)

# number1 = '(221)842-4315x85045'
# number1='0015987465970'


# new_regex = re.sub('[^0-9]+', '', new_format1)
# result = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" % int(new_number_list[:-1])) + new_number_list[-1]
# print(result)



# fake.add_provider(WebProvider)
# address='032 May Motorway Apt. 390\nAndreahaven, ND 68555'
# new_address = address.rstrip()

# print(seperate_address)

# address=str(fake.address())
# address_seperate=re.split('\n|, ', address)
# state = address_seperate[2].split(' ')[0]
# print(f'location: {address_seperate[0]}, city:{address_seperate[1]}, state:{state}')

def split_info(item):
# def generate_data(num):
    pass
#id = random.sample(range(1, 21), 20) 
#name = random.choices(restaurant_list)
#address=fake.address() #9942 Beth Drive Apt. 811 Harperchester, GA 16790
#city
#state
#phone=fake.phone_number() #001-735-019-4897
#genres=random.choices(genre_choices)
#website=fake.url() or "www"+name+.com
#facebook_link="www.fcebook.com/"+name
#seeking_talent =bool(random.getrandbits(1))
#seeking_talent_description = random.choice(seeking_description)  ->if the seeking_talent is true



#artist_image url:fake.image_url()
#fake.email()
