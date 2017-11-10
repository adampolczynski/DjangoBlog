from django.db import models

# Create your models here.


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # exclude = ['author', 'updated', 'created', ]
        fields = ['text', 'email']
        widgets = {
            'text': forms.TextInput(
                attrs={'id': 'post', 'required': True, }
            ),
        }