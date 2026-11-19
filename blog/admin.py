from django.contrib import admin


from .models import Post, Tag, Author

# Register your models here.


admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tag)