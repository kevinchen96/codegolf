from django import forms

class ProblemForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    test_in = forms.CharField()
    test_out = forms.CharField()
