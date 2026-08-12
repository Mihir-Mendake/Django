from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound
from django.urls import reverse
#from django.template.loader import render_to_string
# Create your views here.

blog_names = {
    "python-intro": "Python Post",
    "django-basics": "Django Blog Post",
    "python-oops": "Object Oriented Programming with Python",
    "regex": "Regular Expression in Python"
}


def home_page(request):
    return render(request, "blog/index.html")
    # res_data = render_to_string("blog/index.html")
    # return HttpResponse(res_data)


def blogposts(request):
    list_items = ""
    blog_list = list(blog_names.keys())
    for b in blog_list:
        blog_path = reverse("blog-post", args=[b])
        list_items += f'<li><a href="{blog_path}">{b.capitalize()}</a></li>'

    res_data =f"<ul>{list_items}</ul>"
    return HttpResponse(res_data)

def process_blog_name(blog):
    blog_list = blog.split("-")
    return " ".join(blog_list).title()

def blog_post(request, blog):
    try:
       res = blog_names[blog]
       return render(request, "blog/posts.html",{"blog_text":res , "blog_names":process_blog_name(blog)} )
    except Exception:
        return HttpResponseNotFound("<h1>Blog not found</h1>")




# def blog_post_by_number(request, blog):
#     return HttpResponse(blog)

# if blog == "python_intro":
    #     res = "<h1>Python Post</h1>"
    # elif blog == "django_basics":
    #     res = "<h1>Django Blog Post</h1>"
    # elif blog == "python_oops":
    #     res = "<h1>Object Oriented Programming with Python</h1>"
    # else:

# """
# <ul>
#     <li><a href="allposts/python_intro">Python Intro</a></li>
#     <li><a href="allposts/python_oops">/a>Object Oriented Programming with Python</li>
#     <li><a href="allposts/regex">Regular Expression in Python</a></li>
# </ul>
# """ used in blogpost