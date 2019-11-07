from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    votes_total = models.SmallIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:100]



class Comment(models.Model):
    class Meta:
        db_table = "comments"

    path = ArrayField(models.IntegerField())
    post_id = models.ForeignKey(Post,on_delete=models.PROTECT)
    user_id = models.ForeignKey(User,on_delete=models.PROTECT)
    content = models.TextField('Комментарий')
    pub_date = models.DateTimeField('Дата комментария', default=timezone.now)

    def __str__(self):
        return self.content[0:200]

    def get_offset(self):
        level = len(self.path) - 1
        if level > 5:
            level = 5
        return level

    def get_col(self):
        level = len(self.path) - 1
        if level > 5:
            level = 5
        return 12 - level

