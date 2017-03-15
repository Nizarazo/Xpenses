from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100, required=False)
    age = forms.IntegerField()
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea())
