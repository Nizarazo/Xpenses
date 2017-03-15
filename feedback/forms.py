from django import forms

CATEGORIES = (
    ('probelm', 'Problem in website'),
    ('suggestion', 'Site Suggestion'),
    ('other', 'Other...'),
)


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100, required=False)
    age = forms.IntegerField()
    email = forms.EmailField()
    category = forms.ChoiceField(CATEGORIES)
    content = forms.CharField(widget=forms.Textarea())
