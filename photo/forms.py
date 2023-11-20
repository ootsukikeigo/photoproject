from django.forms import ModelForm
from .models import PhotoPost

class PhotoPostForm(ModelForm):
    class Meta:
        model=PhotoPost
        fields=['Category','title','comment','imagi1','image2']