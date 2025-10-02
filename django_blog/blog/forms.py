from taggit.forms import TagWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post ,Tag
from .models import Comment

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

        

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets ={ 'tags': TagWidget(),
                  }
    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }

class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Comma-separated tags")

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            tag_names = self.cleaned_data['tags'].split(',')
            tag_objects = []
            for name in tag_names:
                name = name.strip()
                if name:
                    tag_obj, created = Tag.objects.get_or_create(name=name)
                    tag_objects.append(tag_obj)
            instance.tags.set(tag_objects)
        return instance
    

