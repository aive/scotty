from django import template
from dog.models import Region
from dog.models import Cottage

register = template.Library()

@register.inclusion_tag('dog/regs.html')
def get_region_list(reg=None):
     return {'regs': Region.objects.all(),
             'act_reg': reg}

@register.inclusion_tag('dog/searchresults.html')
def get_cottage_list():
    return {'cottages': Cottage.objects.all()}
