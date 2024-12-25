from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django_ckeditor_5.fields import CKEditor5Field 


class Post(models.Model):
    image = models.ImageField('Image', upload_to='images/', null=True, blank=True, default='defaults/default-thumbnail.png')
    thumbnail = ImageSpecField(source="image", processors=[ResizeToFill(540,300)], format='JPEG', options={'quality': 60})
    title = models.CharField('Title', max_length=200, null=True, blank=True)
    description = models.TextField('Description', max_length=500, null=True, blank=True)
    content = CKEditor5Field('Context', config_name='extends', null=True, blank=True)
    last_update = models.DateTimeField('Last Update', auto_now=True, null=True)
    created = models.DateTimeField('Created', auto_now_add=True, null=True)

    def get_cached_image(self):
        return ImageCacheFile(self.thumbnail)   