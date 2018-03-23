from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.urlresolvers import reverse
import os
from django.contrib.staticfiles import finders
from dog.models import Cottage, Region
import populate_script
from dog.forms import CottageForm, RegionForm

class Cottage(TestCase):
    #Test validating that "add_cottage" link only appears in valid Regions
    def test_link_to_add_cottage_only_appears_in_valid_regions(self):
            # Access a cottage that does not exist
            response = self.client.get(reverse('dog:show_cottage', args=['python']))

            # Check that there is not a link to add cottage
            try:
                self.assertNotIn(reverse('add_cottage', args=['python']), response.content.decode('ascii'))
                # Access a region that does not exist
                response = self.client.get(reverse('dog:show_region', args=['other-frameworks']))
                # Check that there is not a link to add cottage
                self.assertNotIn(reverse('add_cottage', args=['other-frameworks']), response.content.decode('ascii'))
            except:
                try:
                    self.assertNotIn(reverse('dog:add_cottage', args=['python']), response.content.decode('ascii'))
                    # Access a region that does not exist
                    response = self.client.get(reverse('dog:show_cottage', args=['other-frameworks']))
                    # Check that there is not a link to add cottage
                    self.assertNotIn(reverse('dog:add_cottage', args=['other-frameworks']), response.content.decode('ascii'))
                except:
                    return False
    
    #Test that Browse COttages page contaings the intro message  
    def test_browse_cottage_displays_message(self):
        # Check if there is the message 'Here are some wonderful dogfriendly cottages in the region. Check them out!'
        response = self.client.get(reverse('dog:browse_cottages'))
        self.assertIn('Here are some wonderful dogfriendly cottages in the region. Check them out!'.lower(), response.content.decode('ascii').lower())

    # Test checking that Regions page is using a template
    def test_region_page_is_using_template(self):
        self.client.get(reverse('index'))
        response = self.client.get(reverse('dog:regions'))

        # Check the template used to render regions page
        self.assertTemplateUsed(response, 'dog/regions.html')

    # Test checking the use of background pic in the regions page
    def test_regions_page_is_using_background_pic(self):
        response = self.client.get(reverse('dog:regions'))

        # Check if is there a background image in the html
        self.assertIn('background-image: url("/static/images/background.png")'.lower(), response.content.decode('ascii').lower())