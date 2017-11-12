from django import forms

class CommentForm(forms.Form):
    id = forms.IntegerField() # id of entry or article, got from template
    user = forms.CharField(max_length=20)
    type = forms.CharField(max_length=10) # entry or article
    body = forms.CharField(max_length=120, widget=forms.Textarea)

   