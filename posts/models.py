from django.db import models


class Post(models.Model):
    author = models.CharField('작성자', max_length=20)
    contents = models.TextField('글내용', max_length=1000)

    def __str__(self):
        return self.contents
