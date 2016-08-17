# -*- coding: utf-8 -*-
from django.conf import settings
import json

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import GeonodeCmsMapPlugin
from .forms import GeonodeMapSelectForm
from geonode.maps.models import MapLayer


class GeonodePlugin(CMSPluginBase):
    form = GeonodeMapSelectForm
    name = u'Geonode map'
    model = GeonodeCmsMapPlugin
    render_template = 'geonode_cms_map/_geonode_cms_map_plugin.html'
    text_enabled = True


    def render(self, context, instance, placeholder):
        layers = MapLayer.objects.filter(map_id=instance.geonode_map_id).exclude(group=u'background')
        for layer in layers:
            layer.name = layer.name[8:]
            layer.title = json.loads(layer.layer_params)['title']

        context['instance'] = instance
        context['layers'] = layers
        return context

    def icon_src(self, instance):
        return settings.STATIC_URL + 'geonode_cms_map/images/geonode_plugin_icon_inv.png'

    def icon_alt(self, instance):
        return u'%s' % instance

plugin_pool.register_plugin(GeonodePlugin)