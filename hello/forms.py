from django import forms

from hello.models import LogMessage

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("Mensaje",)  # NOTE: the trailing comma is required
