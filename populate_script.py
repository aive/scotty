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
    {"title": "Aberdeenshire", "address":"AB1","views": 20},
    {"title": "Applecross", "address":"IV54","views": 21},
    {"title": "Stirling", "address":"FK15","views": 10},
    {"title": "Alvemore","address":"PH22","views": 220},
    {"title": "BettyHill", "address":"KW14","views": 10},
    {"title": "Braemar", "address":"AB35","views": 520},
    {"title": "Cannich", "address":"IV4","views": 520},
    {"title": "Corpach","address":"PH33","views": 820},
    {"title": "Dalwhinnie", "address":"PH19","views": 22},
    {"title": "Edderton","address":"IV19", "views": 20}

    ]

        
    lowlands_cottages = [
    {"title": "Guildford", "address":"GU4","views": 20},
    {"title": "Hudderfield", "address":"HD2","views": 21},
    {"title": "Dunbane", "address":"FK15","views": 10},
    {"title": "Hereford", "address":"HR2","views": 10},
    {"title": "Beauly", "address":"IV4","views": 520},
    {"title": "Ayr", "address":"KA7","views": 420},
    {"title": "Cupar", "address":"KY15", "views": 20}
    ]


    islands_cottages = [
    {"title": "Belfast","address":"BT1","views": 20},
    {"title": "Newcastle","address":"BT33","views": 21},
    {"title": "Ballymena","address":"BT44","views": 10},
    {"title": "Newtownnards","address":"BT52","views": 230},
    {"title": "Dungannon", "address":"BT70","views": 12},
    {"title": "Isle of Man","address":" IM3","views": 520},
    {"title": "Isles of Scilly","address":"TR23","views": 230}

    ]


    regs = {"Highlands": {"cottages": highlands_cottages, "views": 128, "likes": 64},
            "Lowlands": {"cottages": lowlands_cottages, "views": 64, "likes": 32},
            "Islands": {"cottages": islands_cottages, "views": 32, "likes": 16}}

    for reg, reg_data in regs.items():
        r = add_reg(reg, reg_data["views"], reg_data["likes"])
        for c in reg_data["cottages"]:
            add_cottage(r, c["title"], c["address"], c["views"])
        
    for r in Region.objects.all():
        for c in Cottage.objects.filter(region=r):
            print("- {0} - {1}".format(str(r), str(c)))


def add_cottage(reg, title, address, views=0):
        c = Cottage.objects.get_or_create(region=reg, title=title)[0]
        c.address=address
        c.save()
        return c

def add_reg(name, views=0, likes=0):
        r = Region.objects.get_or_create(name=name)[0]
        r.name=name
        r.save()
        return r

if __name__ == '__main__':
        print("Starting BnB population script...")
        populate()

