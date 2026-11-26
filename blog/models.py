from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()


    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


    def __str__(self):
        return self.get_full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=100)
    preview = models.CharField(max_length=250)
    content = models.TextField()
    date = models.DateTimeField(auto_now=True , editable=False)
    slug = models.SlugField(unique=True)
    image = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL , null = True)
    tags = models.ManyToManyField(Tag)


class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    comment_text = models.TextField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
