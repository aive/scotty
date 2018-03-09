from django import template
from dog.models import Region

register = template.Library()

@register.inclusion_tag('dog/regs.html')
def get_region_list(reg=None):
     return {'regs': Region.objects.all(),
             'act_reg': reg}
