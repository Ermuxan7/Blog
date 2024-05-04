from django.db import models
from django.urls import reverse


class Category(models.Model):

    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
    # def get_absolute_url(self):
    #     return reverse('category', args=[self.id])
    
    class Meta:
        verbose_name='Category'
        verbose_name_plural='Category'



class vlog(models.Model):

    title=models.CharField(max_length=20)
    slug=models.SlugField()
    description=models.TextField()
    image=models.ImageField(upload_to='images/')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='vlog'
        verbose_name_plural='vlog'
