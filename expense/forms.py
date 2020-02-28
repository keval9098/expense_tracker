from django import forms

class Add_form(forms.Form):
    spent_on = forms.CharField(label='Spent on', max_length=100)
    reason = forms.CharField(label='Reason', max_length=100)
    amount = forms.IntegerField(max_value=10, min_value=1)
