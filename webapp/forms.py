from django import forms
from webapp.models import production
from django.contrib.auth import (
    authenticate,
    get_user_model

)


class productionForm(forms.Form):
    class Meta:
        model=production
        fields='__all__'