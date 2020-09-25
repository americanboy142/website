from PIL import Image
from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate
from .forms import PostForm

class PostyForm(PostForm):
    author = models.ForeignKey(User, on_delete= models.CASCADE, null=True, blank=True )
    text = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    up_file = models.FileField()

    class Meta:
        model = Post
        fields = ['author', 'text', 'file', 'published_date']