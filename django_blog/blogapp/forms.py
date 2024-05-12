from django import forms
from .models import Post, Category, Comment


choice = Category.objects.all().values_list('name' , 'name')
lists = []

for item in choice:
    lists.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title' , 'author', 'category' , 'body', 'header_image') #add snippet to fields if needed and uncomment in maodels.py file

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Enter Title'}),
            'author' : forms.TextInput(attrs={'class':'form-control' ,'value':'','id':'user','type':'hidden'}),
            # 'author' : forms.Select(attrs={'class':'form-control'}),
            'category' : forms.Select(choices=lists,attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control' , 'placeholder':'Describe the Title'}),
            # 'snippet' : forms.Textarea(attrs={'class':'form-control' , 'placeholder':'Describe the Title'}),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'header_image')

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Enter Title'}),
            'body' : forms.Textarea(attrs={'class':'form-control' , 'placeholder':'Describe the Title'}),
            
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Enter Name'}),
            'body' : forms.Textarea(attrs={'class':'form-control' , 'placeholder':'Describe!!! your comment'}),
        }