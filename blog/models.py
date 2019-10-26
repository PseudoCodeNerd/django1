from django.db import models
from django.conf import settings
from django.utils import  timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_data = models.DateTimeField(default=timezone.now)
    published_data = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_data = timezone.now()
        self.save()

    def __str__(self):
        return self.title

'''
class Post(models.Model): – this line defines our model (it is an object).

    class is a special keyword that indicates that we are defining an object.
    Post is the name of our model. We can give it a different name (but we must avoid special characters and whitespace). Always start a class name with an uppercase letter.
    models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database.


    models.CharField – this is how you define text with a limited number of characters.
    models.TextField – this is for long text without a limit. Sounds ideal for blog post content, right?
    models.DateTimeField – this is a date and time.
    models.ForeignKey – this is a link to another model.

'''