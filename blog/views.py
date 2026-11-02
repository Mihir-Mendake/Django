from django.shortcuts import render
from django.http import Http404 , HttpResponseNotFound
from django.urls import reverse
from datetime import date
from django.template.loader import render_to_string
# Create your views here.

blog_details = [
 {
    "slug": "python-intro",
    "image": "python.png",
    "date": date(2025,10,16),
    "title": "Python Introduction",
    "preview": """Pythoon is a open source, high level programming language that is used widely.
    Application of pythons are software development , data science,AI & ML, etc.""" ,
    "content": """Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. 
    Its high-level built in data structures, combined with dynamic typing and dynamic binding,
    make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. 
    Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance."""
 },
 {
    "slug": "django-basics",
    "image": "django.jpg",
    "date": date(2025, 10, 17),
    "title": "Django Blog Post",
    "preview": """Django is a high-level Python web framework that encourages rapid development
    and clean, pragmatic design. It handles much of the complexity of web development,
    so you can focus on writing your app.""",
    "content": """Django is a free and open-source web framework written in Python that follows
    the model–template–views (MTV) architectural pattern. It is maintained by the Django Software
    Foundation. Django's primary goal is to ease the creation of complex, database-driven websites.
    It emphasizes reusability and pluggability of components, less code, low coupling, rapid development,
    and the principle of don't repeat yourself (DRY). Python is used throughout, even for settings,
    files, and data models."""
 },
 {
    "slug": "python-oops",
    "image": "oops.png",
    "date": date(2025, 10, 18),
    "title": "Object Oriented Programming with Python",
    "preview": """Object Oriented Programming (OOP) is a programming paradigm that organizes
    software design around data, or objects, rather than functions and logic.
    Python fully supports OOP with classes, inheritance, encapsulation, and polymorphism.""",
    "content": """Object-Oriented Programming (OOP) in Python is a way of structuring programs
    by bundling related properties and behaviors into individual objects. The four pillars of OOP
    are Encapsulation, Abstraction, Inheritance, and Polymorphism. In Python, everything is an object,
    and classes act as blueprints for creating objects. OOP makes code more modular, reusable, and
    easier to maintain. Python's straightforward syntax makes it one of the best languages to learn
    and apply OOP concepts effectively."""
 },
 {
    "slug": "regex",
    "image": "regex.png",
    "date": date(2025, 10, 19),
    "title": "Regular Expression in Python",
    "preview": """Regular Expressions (RegEx) are sequences of characters that define a search pattern.
    Python provides the built-in 're' module to work with regular expressions for pattern matching
    and string manipulation.""",
    "content": """A Regular Expression (RegEx) is a special sequence of characters that helps you
    match or find other strings or sets of strings, using a specialized syntax held in a pattern.
    Python's built-in 're' module provides full support for Perl-like regular expressions. RegEx is
    widely used for input validation, web scraping, text parsing, and search-and-replace operations.
    Common methods include re.match(), re.search(), re.findall(), and re.sub(). Mastering RegEx
    can greatly simplify complex string processing tasks in Python."""
 }
]




def home_page(request):
    sorted_blogs = sorted(blog_details, key=lambda post:post["date"], reverse = True)
    latest_blogs = sorted_blogs[:2]
    return render(request, "blog/index.html", {"l_blogs":latest_blogs})
    # res_data = render_to_string("blog/index.html")
    # return HttpResponse(res_data)




def blogposts(request):
    return render(request, "blog/allposts.html", {"blogs":blog_details})

    for b in blog_list:
        blog_path = reverse("blog-post", args=[b])
        list_items += f'<li><a href="{blog_path}">{b.capitalize()}</a></li>'

    res_data =f"<ul>{list_items}</ul>"
    return HttpResponse(res_data)



def process_blog_name(blog):
    blog_list = blog.split("-")
    return " ".join(blog_list)




def blog_post(request, blog):
    try:
       res = blog_names[blog]
       return render(request, "blog/posts.html",
                     {"blog_text":res , "blog_names":process_blog_name(blog)} )
    except Exception:
        raise Http404()





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