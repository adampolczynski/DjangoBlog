from django import forms

class CommentForm(forms.Form):
    id = forms.IntegerField()
    type = forms.CharField(max_length=10)
    # entry or article
    body = forms.CharField(max_length=120, widget=forms.Textarea)

   