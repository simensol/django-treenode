# -*- coding: utf-8 -*-

from django import forms

from .utils import split_pks


class TreenodeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TreenodeForm, self).__init__(*args, **kwargs)
        exclude_pks = []
        obj = self.instance
        if obj.pk:
            exclude_pks += [obj.pk]
            exclude_pks += split_pks(obj.tn_descendants_pks)
        manager = obj.__class__.objects
        self.fields['tn_parent'].queryset = manager.exclude(pk__in=exclude_pks)