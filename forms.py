# -*- coding: utf-8 -*-

from django.forms.models import ModelForm

from geonode.maps.models import Map

class GeonodeMapSelectForm(ModelForm):
    """
    Provides the user with a dropdown choice of the available genoode maps.
    """

    class Meta:
        model = Map
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GeonodeMapSelectForm, self).__init__(*args, **kwargs)

        def get_choices():
            values = Map.objects.values_list('title').order_by('title')
            return values

