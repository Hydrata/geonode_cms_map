# -*- coding: utf-8 -*-
from django.db import models

from cms.models import CMSPlugin
import geonode.maps


class GeonodeCmsMapPlugin(CMSPlugin):

    geonode_server = models.CharField(
        'Geonode Server',
        max_length='200',
        default='http://chennaifloodmanagement.org',
        blank=False,
        help_text=u'Geonode server address like this - http://example.com'
    )

    geonode_map_id = models.IntegerField(
        'Geonode Map ID',
        blank=False,
        help_text=u'Geonode Map ID. To get this, read the number after the word "/maps/" in the URL of your geonode map'
        # TODO this can be improved by pinging the geonode API and proving a dropdown list of available maps
    )

    geonode_map_caption = models.CharField(
        'Caption',
        max_length='512',
        blank=True,
        help_text=u'A caption for your map'
    )

    geonode_map_width = models.IntegerField(
        'Map Width (%)',
        default='100',
        blank=False,
        help_text=u'Map width as a percentage of the available browser space'
    )

    geonode_map_height = models.IntegerField(
        'Map Height (pixels)',
        blank=False,
        default='800',
        help_text=u'Map height in pixels.'
    )

    def __unicode__(self):
        return u'Map ID - %s' % (self.geonode_map_id)