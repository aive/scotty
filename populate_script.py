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
    {"name": "The Burrow", "area":"Aberdeenshire", "image": "cottages/The Burrow.jpg", "address":"AB51 4GY","views": 20},
    {"name": "Windyridge", "area": "Applecross", "image": "cottages/Windyridge.jpg", "address":"IV54 8LR","views": 21},
    {"name": "Garden Cottage", "area": "Stirling", "image": "cottages/Garden Cottage.jpg", "address":"FK15 0HG","views": 10},
    {"name": "Four Winds", "area": "Aviemore", "image": "cottages/Four Winds.jpg","address":"PH22 1RB","views": 220},
    {"name": "Wild Bank", "area": "BettyHill", "image": "cottages/Wild Bank.jpg", "address":"KW14 8TY","views": 10},
    {"name": "Mile End", "area": "Braemar", "image": "cottages/Mile End.jpg", "address":"AB35 5XU","views": 520},
    {"name": "Dreamwood", "area": "Cannich", "image": "cottages/Dreamwood.jpg", "address":"IV4 7HR","views": 520},
    {"name": "Stillness", "area": "Corpach", "image": "cottages/Stillness.jpg","address":"PH33 6PF","views": 820},
    {"name": "Bridgelands", "area": "Dalwhinnie", "image": "cottages/Bridgelands.jpg", "address":"PH19 1AA","views": 22},
    {"name": "Dengarden", "area": "Edderton", "image": "cottages/Dengarden.jpg","address":"IV19 1EH", "views": 20}

    ]



    lowlands_cottages = [
    {"name": "Kuredu", "area":"Guildford", "image": "cottages/Kuredu.jpg", "address":"GU4 8SE","views": 20},
    {"name": "Cumfrubrum", "area":"Hudderfield", "image": "cottages/Cumfrubrum.jpg", "address":"HD2 1YY","views": 21},
    {"name": "Chestnuts", "area":"Dunbane", "image": "cottages/Chestnuts.jpg", "address":"FK15 0NB","views": 10},
    {"name": "The Warren", "area":"Hereford", "image": "cottages/The Warren.jpg", "address":"HR2 6JT","views": 10},
    {"name": "The Cuckoo's Nest", "area":"Beauly", "image": "cottages/The Cuckoo's Nest.jpg", "address":"IV40 8DX","views": 520},
    {"name": "Crystal Cottage", "area":"Ayr", "image": "cottages/Crystal Cottage.jpg", "address":"KA7 4PQ","views": 420},
    {"name": "Kites Farm", "area":"Cupar", "image": "cottages/Kites Farm.jpg", "address":"KY15 7HY", "views": 20}
    ]

    islands_cottages = [
    {"name": "Robins Hedge", "area":"Belfast", "image": "cottages/Robins Hedge.jpg","address":"BT18 9JQ","views": 20},
    {"name": "Heatherbell", "area":"Newcastle", "image": "cottages/Heatherbell.jpg","address":"BT3 9JL","views": 21},
    {"name": "Chimney Cottage", "area":"Ballymena", "image": "cottages/Chimney Cottage.jpg","address":"BT44 8SB","views": 10},
    {"name": "Rosemary House", "area":"Newtownnards", "image": "cottages/Rosemary House.jpg","address":"BT52 2NS","views": 230},
    {"name": "Mulberry", "area":"Dungannon", "image": "cottages/Mulberry.jpg", "address":"BT70 2HW","views": 12},
    {"name": "Stonehurst", "area":"Isle of Man", "image": "cottages/Stonehurst.jpg","address":"IM3 1BB","views": 520},
    {"name": "Seacrest", "area":"Isles of Scilly", "image": "cottages/Seacrest.jpg","address":"TR23 0WA","views": 230}

    ]




    regs = {"Highlands": {"cottages": highlands_cottages, "views": 128, "likes": 64},
            "Lowlands": {"cottages": lowlands_cottages, "views": 64, "likes": 32},
            "Islands": {"cottages": islands_cottages, "views": 32, "likes": 16}}


    for reg, reg_data in regs.items():
        r = add_reg(reg, reg_data["views"], reg_data["likes"])
        for c in reg_data["cottages"]:
            add_cottage(r, c["name"], c["address"], c["views"])


    for cottage in islands_cottages:
        cottage_object = Cottage.objects.get_or_create(name=cottage['name'])[0]
        cottage_object.image = cottage['image']
        cottage_object.save()

        print(cottage_object)

        print(cottage)

    print('=====')

    for cottage in lowlands_cottages:
        cottage_object = Cottage.objects.get_or_create(name=cottage['name'])[0]
        cottage_object.image = cottage['image']
        cottage_object.save()

        print(cottage_object)

        print(cottage)

    print('=====')

    for cottage in highlands_cottages:
        cottage_object = Cottage.objects.get_or_create(name=cottage['name'])[0]
        cottage_object.image = cottage['image']
        cottage_object.save()

        print(cottage_object)

        print(cottage)

    print('=====')



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

def add_review(cottage_object, name, comment, date_added):
        comment = Comment.objects.get_or_create(comment=com, name=name)[0]
        com.comment=comment
        com.date_added=date_added
        com.save()
        return comment


if __name__ == '__main__':
        print("Starting population script...")
        populate()
