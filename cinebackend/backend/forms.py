from django import forms

LANG_CHOICES = (('OV','OV'),('OmU','OmU'),('OmeU','OmeU'),('dt. Synchro','dt. Synchro'),)
LOC_CHOICES = (('Kinobar','Kinobar'),('Sommerkino auf der Feinkost','Sommerkino auf der Feinkost'))

class NewTimeForm(forms.Form):
    language = forms.ChoiceField(choices=LANG_CHOICES, label="Sprachversion auswählen")
    location = forms.ChoiceField(choices=LOC_CHOICES, label="Ort auswählen")
    premiere = forms.ChoiceField(choices=(('True', 'Ja'), ('False', 'Nein')), widget=forms.RadioSelect)