from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        # fields = ('title', 'content',)
        fields = '__all__'
        exclude = ('created_by', )


class BlogFormBak(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField()

    def clean_title(self):
        print('cleaning title')
        title = self.cleaned_data.get('title')
        return title.strip()

    def clean_content(self):
        print('cleaning content')
        content = self.cleaned_data.get('content')
        return content.strip()

    def clean(self):
        print('cleaning ...')

    def save(self):
        title = self.cleaned_data.get('title')
        content = self.cleaned_data.get('content')

        blog = Blog.objects.create(title=title, content=content)

        return blog