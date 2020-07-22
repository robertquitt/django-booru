# -*- coding: utf-8 -*-

from django import forms


class ImageUploadForm(forms.Form):
    image_file = forms.ImageField(
        label='Select a file',
    )
