import sys
sys.path.append('..')

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'dog_project.settings')
import django
django.setup()
from dog.models import Region
from dog.models import Cottage

def populate():
    
    highlands_cottages = [
    {"name": "Aberdeenshire", "image": "cottages/Aberdeenshire.jpg", "address":"AB51 4GY","views": 20},
    {"name": "Applecross", "image": "cottages/Applecross.jpg", "address":"IV54 8LR","views": 21},
    {"name": "Stirling", "image": "cottages/Stirling.jpg", "address":"FK15 0HG","views": 10},
    {"name": "Alvemore", "image": "cottages/Alvemore.jpg","address":"PH22 1RB","views": 220},
    {"name": "BettyHill", "image": "cottages/BettyHill.jpg", "address":"KW14 8TY","views": 10},
    {"name": "Braemar", "image": "cottages/Braemar.jpg", "address":"AB35 5XU","views": 520},
    {"name": "Cannich", "image": "cottages/Cannich.jpg", "address":"IV4 7HR","views": 520},
    {"name": "Corpach", "image": "cottages/Corpach.jpg","address":"PH33 6PF","views": 820},
    {"name": "Dalwhinnie", "image": "cottages/Dalwhinnie.jpg", "address":"PH19 1AA","views": 22},
    {"name": "Edderton", "image": "cottages/Edderton.jpg","address":"IV19 1EH", "views": 20}

    ]
    for cottage in highlands_cottages:

        cottage_object = Cottage.objects.get_or_create(name=cottage['name'])[0]
        cottage_object.image = cottage['image']
        cottage_object.save()

        print(cottage_object)
        
        print(cottage)

    print('=====')


    
    lowlands_cottages = [
    {"name": "Guildford", "image": "cottages/Guildford.jpg", "address":"GU4 8SE","views": 20},
    {"name": "Hudderfield", "image": "cottages/Hudderfield.jpg", "address":"HD2 1YY","views": 21},
    {"name": "Dunbane", "image": "cottages/Dunbane.jpg", "address":"FK15 0NB","views": 10},
    {"name": "Hereford", "image": "cottages/Hereford.jpg", "address":"HR2 6JT","views": 10},
    {"name": "Beauly", "image": "cottages/Beauly.jpg", "address":"IV40 8DX","views": 520},
    {"name": "Ayr", "image": "cottages/Ayr.jpg", "address":"KA7 4PQ","views": 420},
    {"name": "Cupar", "image": "cottages/Cupar.jpg", "address":"KY15 7HY", "views": 20}
    ]
    for cottage in lowlands_cottages:
        cottage_object = Cottage.objects.get_or_create(name=cottage['name'])[0]
        cottage_object.image = cottage['image']
        cottage_object.save()

        print(cottage_object)
        
        print(cottage)

    print('=====')

    islands_cottages = [
    {"name": "Belfast", "image": "cottages/Belfast.jpg","address":"BT18 9JQ","views": 20},
    {"name": "Newcastle", "image": "cottages/Newcastle.jpg","address":"BT3 9JL","views": 21},
    {"name": "Ballymena", "image": "cottages/Ballymena.jpg","address":"BT44 8SB","views": 10},
    {"name": "Newtownnards", "image": "cottages/Newtownnards.jpg","address":"BT52 2NS","views": 230},
    {"name": "Dungannon", "image": "cottages/Dungannon.jpg", "address":"BT70 2HW","views": 12},
    {"name": "Isle of Man", "image": "cottages/Isle of Man.jpg","address":"IM3 1BB","views": 520},
    {"name": "Isles of Scilly", "image": "cottages/Isles of Scilly.jpg","address":"TR23 0WA","views": 230}

    ]
    for cottage in islands_cottages:
        cottage_object = Cottage.objects.get_or_create(name=cottage['name'])[0]
        cottage_object.image = cottage['image']
        cottage_object.save()

        print(cottage_object)
        
        print(cottage)

    print('=====')

    


    regs = {"Highlands": {"cottages": highlands_cottages, "views": 128, "likes": 64},
            "Lowlands": {"cottages": lowlands_cottages, "views": 64, "likes": 32},
            "Islands": {"cottages": islands_cottages, "views": 32, "likes": 16}}

    
    for reg, reg_data in regs.items():
        r = add_reg(reg, reg_data["views"], reg_data["likes"])
        for c in reg_data["cottages"]:
            add_cottage(r, c["name"], c["address"], c["views"])

    


    
    for r in Region.objects.all():
        for c in Cottage.objects.filter(region=r):
            print("- {0} - {1}".format(str(r), str(c)))

    
    

def add_cottage(reg, name, address, views=0):
        c = Cottage.objects.get_or_create(region=reg, name=name)[0]
        c.address=address
        c.save()
        return c

def add_reg(name, views=0, likes=0):
        r = Region.objects.get_or_create(name=name)[0]
        r.name=name
        r.save()
        return r

if __name__ == '__main__':
        print("Starting population script...")
        populate()
