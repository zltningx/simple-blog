from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25,
                           widget=forms
                           .TextInput(attrs={'class': 'form-control'}),
                           label='姓名')
    email = forms.EmailField(widget=forms
                             .TextInput(attrs={'class': 'form-control'}),
                             label='您的邮箱')
    to = forms.EmailField(widget=forms.
                          TextInput(attrs={'class': 'form-control'}),
                          label='发送邮箱')
    comments = forms.CharField(required=False,
                               widget=forms.
                               Textarea(attrs={'class': 'form-control'}),
                               label='评论')


class CommentForm(forms.ModelForm):
    name = forms.CharField(max_length=25,
                           widget=forms.
                           TextInput(attrs={'class': 'form-control'}),
                           label='姓名')
    email = forms.EmailField(widget=forms.
                             TextInput(attrs={'class': 'form-control'}),
                             label='邮箱')
    body = forms.CharField(
            widget=forms.Textarea(attrs={'class': 'form-control'}), label='评论')

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')