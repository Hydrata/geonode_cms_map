# -*- coding: utf-8 -*-
from    django.conf import settings

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import GeonodeCmsMapPlugin

class GeonodePlugin(CMSPluginBase):
    name=u'Geonode map'
    model = GeonodeCmsMapPlugin
    render_template = 'geonode_cms_map/_geonode_cms_map_plugin.html'
    text_enabled = True

    def render(self, context, instance, placeholder):

        context['instance'] = instance

        return context

    def icon_src(self, instance):
        return settings.STATIC_URL + 'geonode_cms_map/images/geonode_plugin_icon_inv.png'

    def icon_alt(self, instance):
        return u'%s' % instance

plugin_pool.register_plugin(GeonodePlugin)