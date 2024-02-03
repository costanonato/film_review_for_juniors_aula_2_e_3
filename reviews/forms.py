from django import forms


class CommentForm(forms.Form):
    user_name = forms.CharField(max_length=200)
    user_email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
