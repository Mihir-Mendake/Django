from django.shortcuts import render
from django.http import Http404 , HttpResponseNotFound
from .models import Post

# Create your views here.

def home_page(request):
    latest_blogs = Post.objects.all().order_by("-date")[:2] #db
    # sorted_blogs = sorted(blog_details, key=lambda post:post["date"], reverse = True)
    # latest_blogs = sorted_blogs[:2] for dummy data
    return render(request, "blog/index.html", {"l_blogs":latest_blogs})

    # res_data = render_to_string("blog/index.html")
    # return HttpResponse(res_data)

def blogposts(request):
    blog_details = Post.objects.all()
    return render(request, "blog/allposts.html", {"blogs":blog_details})

    for b in blog_list:
        blog_path = reverse("blog-post", args=[b])
        list_items += f'<li><a href="{blog_path}">{b.capitalize()}</a></li>'

    res_data =f"<ul>{list_items}</ul>"
    return HttpResponse(res_data)

def blog_post(request, blog):
    try:
       res = Post.objects.get(slug = blog)
       return render(request, "blog/posts.html",
                     {"post":res})
    except Exception:
        raise Http404()
