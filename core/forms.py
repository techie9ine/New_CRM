from django import forms

from .models import Record


class AddRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ["first_name", "last_name", "email", "phone", "city", "address", "state", "zip_code", "country",
                  "payment_complete"]
