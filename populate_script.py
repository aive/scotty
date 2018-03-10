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
    {"name": "Aberdeenshire", "image": "Aberdeenshire.jpg", "address":"AB1","views": 20},
    {"name": "Applecross", "image": "Applecross.jpg", "address":"IV54","views": 21},
    {"name": "Stirling", "image": "Stirling.jpg", "address":"FK15","views": 10},
    {"name": "Alvemore", "image": "Alvemore.jpg","address":"PH22","views": 220},
    {"name": "BettyHill", "image": "BettyHill.jpg", "address":"KW14","views": 10},
    {"name": "Braemar", "image": "Braemar.jpg", "address":"AB35","views": 520},
    {"name": "Cannich", "image": "Cannich.jpg", "address":"IV4","views": 520},
    {"name": "Corpach", "image": "Corpach.jpg","address":"PH33","views": 820},
    {"name": "Dalwhinnie", "image": "Dalwhinnie.jpg", "address":"PH19","views": 22},
    {"name": "Edderton", "image": "Edderton.jpg","address":"IV19", "views": 20}

    ]


    lowlands_cottages = [
    {"name": "Guildford", "image": "Guildford.jpg", "address":"GU4","views": 20},
    {"name": "Hudderfield", "image": "Hudderfield.jpg", "address":"HD2","views": 21},
    {"name": "Dunbane", "image": "Dunbane.jpg", "address":"FK15","views": 10},
    {"name": "Hereford", "image": "Hereford.jpg", "address":"HR2","views": 10},
    {"name": "Beauly", "image": "Beauly.jpg", "address":"IV4","views": 520},
    {"name": "Ayr", "image": "Ayr.jpg", "address":"KA7","views": 420},
    {"name": "Cupar", "image": "Cupar.jpg", "address":"KY15", "views": 20}
    ]


    islands_cottages = [
    {"name": "Belfast", "image": "Belfast.jpg","address":"BT1","views": 20},
    {"name": "Newcastle", "image": "Newcastle.jpg","address":"BT33","views": 21},
    {"name": "Ballymena", "image": "Ballymena.jpg","address":"BT44","views": 10},
    {"name": "Newtownnards", "image": "Newtownnards.jpg","address":"BT52","views": 230},
    {"name": "Dungannon", "image": "Dungannon.jpg", "address":"BT70","views": 12},
    {"name": "Isle of Man", "image": "Isle of Man.jpg","address":" IM3","views": 520},
    {"name": "Isles of Scilly", "image": "Isles of Scilly.jpg","address":"TR23","views": 230}

    ]
    


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

