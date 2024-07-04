from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    draf=models.BooleanField(default=False)
    img=models.FileField(blank=True, null=True)
    create_date=models.DateTimeField(auto_now_add = True)
    update_date=models.DateTimeField(auto_now = True)
    
    @property
    def formatted_createDate(self):
        return self.create_date.strftime('%Y-%m-%d')
    
    @property
    def formatted_updateDate(self):
        return self.update_date.strftime('%Y-%m-%d')
    
    def __str__(self):
       return self.title
   
   
