# 📝 Blog Site Setup Guide

This guide walks you through building a blog site using Python's Django framework.

---

## 🚀 Step 1: Set Up Project Folder

### 📁 1.1 Create the Project Directory

1. Create a folder named `blog-site`. This will be your main project directory.
2. Open a terminal inside the folder:
   - On **Windows**: Use Command Prompt or PowerShell.
   - On **macOS/Linux**: Use the default terminal.

```bash
mkdir blog-site
cd blog-site
```

---

### 🛠️ 1.2 Initialize Git

#### ✅ Check Git Installation

Ensure Git is installed. If not, download and install it from [git-scm.com](https://git-scm.com/downloads).

#### 🔧 Initialize a Git Repository

```bash
git init
```

#### 📄 Add a `.gitignore` File

Create a `.gitignore` file inside your project folder. Make sure to include common Python exclusions such as:

```plaintext
venv/
__pycache__/
*.pyc
.env
```

Then, stage and commit the `.gitignore`:

```bash
git add .gitignore
git commit -m "initial commit"
```

#### 🌐 Push to GitHub

1. Create a new repository on your GitHub account (e.g., `blog-site`).
2. Follow GitHub’s instructions to push an existing local repo.

```bash
git remote add origin https://github.com/YOUR_USERNAME/blog-site.git
git push -u origin master
```

> Replace `YOUR_USERNAME` with your actual GitHub username.

---

### 🐍 1.3 Set Up Python and Virtual Environment

#### 🔍 Check Python Installation

Make sure Python 3.9 or higher is installed on your system.
You can verify with:

```bash
python --version
```

#### 📦 Install `virtualenv`

If `virtualenv` is not already installed, you can install it using:

```bash
pip install virtualenv
```

#### 🧪 Create and Activate a Virtual Environment

```bash
python -m venv venv
```

> This will create a `venv` folder inside your Project folder.
> All Python dependencies will be installed inside the `venv` folder.
> This folder should be excluded from Git using `.gitignore`.

##### ▶️ Activate the Environment

- **On Windows** (PowerShell):

```powershell
Set-ExecutionPolicy Unrestricted -Scope Process
.\venv\Scripts\activate
```

- **On macOS/Linux**:

```bash
source venv/bin/activate
```

---

## ⚙️ Step 2: Set Up Django

### 📦 2.1 Install Django

Make sure your virtual environment is activated before proceeding.

To install Django:

```bash
pip install django
```

> ✅ Tip: It's a good practice to manage your project dependencies using a `requirements.txt` file. This makes it easy for others (or your future self) to install all required packages with a single command.

To generate the `requirements.txt` file:

```bash
pip freeze > requirements.txt
```

Later, you (or anyone else) can install the dependencies using:

```bash
pip install -r requirements.txt
```

---

### 🏗️ 2.2 Create a New Django Project

Create your Django project named `blog_site`:

```bash
django-admin startproject blog_site .
```

> ⚠️ **Important:** Don’t forget the `.` at the end of the command!
> This ensures the project files are created in the current folder instead of a nested one.

---

### ▶️ 2.3 Run the Development Server

Verify everything is set up correctly by starting the development server:

```bash
python manage.py runserver
```

Now, open your browser and visit:
👉 `http://127.0.0.1:8000/`

You should see the Django welcome page, which confirms your project is working!

---

## 🧱 Step 3: Set Up the `Post` Model

In this step, you'll create a `posts` app and define a `Post` model that represents individual blog posts in your Django application.

---

### 🛠️ 3.1 Create the `posts` App

Django encourages modular design through apps. We'll create a dedicated app named `posts` to handle all blog post-related logic.

```bash
python manage.py startapp posts
```

Now, register the new app in your Django project. Open `blog_site/settings.py` and add `"posts"` to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "posts",  # 👈 Register the posts app here
]
```

---

### 📝 3.2 Define the `Post` Model

Open `posts/models.py` and define the structure of your `Post` model:

```python
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    publish_date = models.DateField()

    def __str__(self):
        return self.title
```

> 🧠 The `__str__` method helps display post titles meaningfully in the admin panel and shell.

Now apply the migrations to create the corresponding database table:

```bash
python manage.py makemigrations
python manage.py migrate
```

> ✅ Tip: After migration, you should see a `posts_post` table in `db.sqlite3`. If you're using VS Code, you can install the **SQLite Viewer** extension to inspect the database directly.

---

### 🧑‍💻 3.3 Register the `Post` Model in the Admin Panel

To manage blog posts through the admin dashboard, register the model in `posts/admin.py`:

```python
from django.contrib import admin
from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "publish_date")


admin.site.register(Post, PostAdmin)
```

> 🖥️ The `list_display` attribute makes the admin list view more informative by showing key fields at a glance.

---

### 🔐 3.4 Access the Admin Panel & Create Posts

#### 🧍 Create a Superuser

Before using the Django admin panel, create a superuser account:

```bash
python manage.py createsuperuser
```

Follow the prompts to enter a username, email, and password.

#### ▶️ Start the Development Server

```bash
python manage.py runserver
```

Visit the Django admin panel at:

👉 `http://127.0.0.1:8000/admin/`

Log in with your superuser credentials.
Then go to:

👉 `http://127.0.0.1:8000/admin/posts/post/`

From there, you can **create, edit, and delete** blog posts through the Django admin interface.

---

## 💬 Step 4: Set Up the `Comment` Model

We'll define a `Comment` model within the existing `posts` app. This keeps things simple, since comments in this case are tightly coupled with posts and don’t have complex logic beyond basic CRUD operations.

---

### 📝 4.1 Define the `Comment` Model

Open `posts/models.py` and add the following `Comment` model definition:

```python
from django.contrib.auth.models import User


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```

> 🔗 Each comment is associated with:
>
> - A `Post` (using a foreign key with cascade delete)
> - A `User` (using Django's built-in User model)

Now, create and apply the migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

> ✅ **Tip:** After migrating, a `posts_comment` table will be created in your SQLite database.

---

### 🧑‍💻 4.2 Register the `Comment` Model in the Admin Panel

To manage comments via the Django admin interface, register the model in `posts/admin.py`:

```python
from posts.models import Post, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "post")


admin.site.register(Comment, CommentAdmin)
```

> 🎛️ Now you'll be able to view, create, and manage comments from the Django admin panel.

---

## ✅ Optional: Set Up `pre-commit` for Code Quality

To maintain clean and consistent code, you can configure [`pre-commit`](https://pre-commit.com/) to automatically run checks before every commit.

### 🧪 What It Does

When set up, `pre-commit` will:

- Remove trailing whitespace
- Ensure files end with a newline
- Format code with **Black**
- Sort imports with **isort**
- Lint code with **Flake8**
- Validate YAML files

### ⚙️ How to Set It Up

1. Make sure you have `pre-commit` installed:

   ```bash
   pip install pre-commit
   ```

2. Add the configuration files:
   - `.pre-commit-config.yaml`
   - `setup.cfg`

   These are already included in your project directory (alongside `README.md`).

3. Install the Git hook:

   ```bash
   pre-commit install
   ```

4. (Optional) Run it on all files immediately:

   ```bash
   pre-commit run --all-files
   ```

---

### ⚠️ Heads-up

- `pre-commit` will **run automatically before every commit**.
- If any check fails, your commit will be blocked until the issues are fixed.
- Either:
  - Run `pre-commit run --all-files` to fix them all at once, or
  - Fix and commit again.

> ✅ This helps catch issues early and ensures your codebase stays clean!

---

## 🏠 Step 5: Set Up the Home Page

Let’s build a simple home page that displays the 5 most recent blog posts.

---

### 🧱 5.1 Create the View

In `posts/views.py`, define a function-based view to retrieve and display recent posts:

```python
from django.shortcuts import render

from .models import Post


def home_view(request):
    """
    Renders the homepage with the 5 most recent blog posts.
    """
    posts = Post.objects.order_by("-id")[:5]
    return render(request, "home.html", {"posts": posts})
```

---

### 🌐 5.2 Connect the URL

Open `blog_site/urls.py` and add the root URL pattern to serve the home page:

```python
from django.contrib import admin
from django.urls import path

from posts.views import home_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
]
```

---

### 🧾 5.3 Create the Template

Inside your project directory, create a `templates` folder (if it doesn’t exist already). Then create a file named `home.html` in that folder.

Your folder structure should look like this:

```plaintext
blog-site/
├── blog_site/
├── posts/
├── templates/
│   └── home.html
```

The `home.html` file should contain basic HTML to loop through and display blog posts. It uses Django’s templating syntax to render each post’s title, content, and publish date.

✅ Now, visiting `http://127.0.0.1:8000/` will show your most recent blog posts rendered with your HTML template.

---

## 📚 Step 6: Create the Post List Page

We’ll now create a dedicated page to display all blog posts. Think of it as your blog’s main directory. Later, we can add features like search, filters, or categories here.

---

### 🧱 6.1 Add the View

In `posts/views.py`, add a new function-based view to retrieve and display all posts:

```python
def post_list_view(request):
    """
    Display the full list of blog posts.
    """
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "post_list.html", context)
```

---

### 🌐 6.2 Connect the URL

Open `blog_site/urls.py` and add a new path for this view:

```python
path("posts/", post_list_view, name="post-list"),
```

Make sure it's added to the same `urlpatterns` list where your home view is registered.

---

### 🧾 6.3 Create the Template

Inside the `templates` folder, create a file named `post_list.html`. This will render the full list of blog posts using a layout similar to `home.html`.

> 💡 While the content might feel similar to the home page, it’s a good practice to keep them separate — the homepage often contains other components (hero section, highlights, etc.), while the post list page is focused solely on browsing all blog entries.

---

### 📝 Note on Truncating Content

In both the `home.html` and `post_list.html` templates, use Django’s `truncatewords` filter to limit the content preview:

```django
<p>{{ post.content|truncatewords:20 }}</p>
```

> ✂️ This ensures that only a short preview (first 20 words) of each blog post is shown. It helps keep the layout clean and scannable, especially when there are long posts. Readers can click into individual posts (which we’ll add soon) to read the full content.

---

## 📰 Step 7: Build the Post Detail Page

When a user clicks on a post title, they should be taken to a page that shows the full content of the post along with any comments. Let’s make that happen.

---

### 🧱 7.1 Create the Detail View

In `posts/views.py`, define a view to fetch and display a single post and its comments:

```python
from django.shortcuts import get_object_or_404, render

from .models import Comment, Post


def post_detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post_id=post_id).select_related("user")

    context = {"post": post, "comments": comments}
    return render(request, "post_detail.html", context)
```

#### 🤔 Why `get_object_or_404`?

Using `get_object_or_404()` is a safer way to retrieve a single post. If no post exists with the given ID, it automatically raises a 404 error, avoiding server crashes from trying to access a non-existent object.

#### 🚀 Why `select_related("user")`?

We use `select_related("user")` when fetching comments to optimize database queries. Since each comment is linked to a user, this fetches the related user data in a single query — preventing the **N+1 query problem** and improving performance.

---

### 🌐 7.2 Add the URL Pattern

Open `blog_site/urls.py` and register the new route:

```python
path("posts/<int:post_id>", post_detail_view, name="post-detail"),
```

---

### 🧾 7.3 Create the Template

Inside the `templates` directory, create `post_detail.html`. This will display the full blog post along with a list of its comments.

At this stage, you can start with something simple like:

```html
<h1>{{ post.title }}</h1>
<p>{{ post.content }}</p>
<p>Published on {{ post.publish_date }}</p>

<hr>
<h3>Comments:</h3>
{% for comment in comments %}
    <p><strong>{{ comment.user.username }}:</strong> {{ comment.content }}</p>
{% empty %}
    <p>No comments yet.</p>
{% endfor %}
```

---

### 🔗 7.4 Make Post Titles Clickable

Update the post titles in both `home.html` and `post_list.html` so that users can navigate to the post detail page:

```html
<h2><a href="{% url 'post-detail' post.id %}">{{ post.title }}</a></h2>
```

---

### 🧪 7.5 Test the Page

1. Start the development server:

   ```bash
   python manage.py runserver
   ```

2. Visit `http://127.0.0.1:8000/`.

3. Click on a post title — you should land on the post detail page showing the full content and its comments.

✅ You now have a basic blog system with a home page, post directory, and individual post pages with comments!

Here’s a clean and concise optional step for setting up `django-debug-toolbar`, including why it’s useful:

---

## 🧰 Optional: Set Up `django-debug-toolbar`

While developing your Django project, it’s often helpful to see what’s happening under the hood — database queries, cache usage, request/response details, and more. This is where `django-debug-toolbar` comes in handy.

---

### 💡 Why Use `django-debug-toolbar`?

`django-debug-toolbar` is a powerful tool that adds a sidebar to your site showing detailed debug information for each page load. It's especially useful for:

- Analyzing database queries (to avoid N+1 issues)
- Tracking performance bottlenecks
- Viewing request headers and session/cookie data
- Debugging templates and static files

---

### ⚙️ How to Install and Configure

#### 1. Install the package

```bash
pip install django-debug-toolbar
```

> 📝 Note: Don’t forget to add django-debug-toolbar==5.1.0 to your requirements.txt file!

---

#### 2. Add it to your Django settings

In `blog_site/settings.py`:

```python
INSTALLED_APPS = [
    # other apps
    "debug_toolbar",
    "posts",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware", # keep this at the top
    # other middlewares
]
```

---

#### 3. Add the toolbar URL pattern

In `blog_site/urls.py`:

```python
from django.conf import settings
from django.urls import include, path

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
```

---

#### 4. Set `INTERNAL_IPS`

Still in `settings.py`, add this so the toolbar knows it's safe to display:

```python
INTERNAL_IPS = ["127.0.0.1"]
```

---

### ✅ You’re Done

Now when you run the server in development (`DEBUG=True`), you’ll see a debug toolbar on the right side of the page. Use it to monitor SQL queries, performance, and much more as you build your blog.

---

## 🎨 Step 8: Add a Portfolio Page

Since this is a personal blog website, it makes sense to have a portfolio page that highlights the author's professional journey and projects.

---

### 8.1: Define the View

Open `posts/views.py` and add the following function:

```python
def portfolio_view(request):
    return render(request, "portfolio.html")
```

> **Note:**
> It doesn’t make sense to create a new Django app just for a simple portfolio page. That’s why we’re placing the view inside the existing `posts` app.

---

### 8.2: Add the URL

Open `blog_site/urls.py` and add the route for the portfolio view:

```python
from posts.views import home_view, portfolio_view, post_detail_view, post_list_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("posts/", post_list_view, name="post-list"),
    path("posts/<int:post_id>/", post_detail_view, name="post-detail"),
    path("portfolio/", portfolio_view, name="portfolio"),
]
```

---

### 8.3: Create the Template

Inside your `templates` directory, create a new file named `portfolio.html`.
You can structure this page however you want to highlight your projects or experience.

---

✅ Now when you visit `http://127.0.0.1:8000/portfolio/` on your local server, it should render the portfolio page.

---

## 🗂️ Step 9: Set Up Static Files

To organize and manage CSS, JavaScript, and images properly, we’ll configure a static files directory in our Django project.

---

### 9.1: Configure Static Files Directory

Open `blog_site/settings.py` and add the following setting:

```python
STATICFILES_DIRS = [Path.joinpath(BASE_DIR, "staticfiles")]
```

This tells Django to look for static files in the `staticfiles` directory inside your project root. You can store CSS, JS, and image files here during development.

---

### 9.2: Move CSS to a Static File

In our previous step, we added some CSS code in `portfolio.html`, it's better to move them into a dedicated CSS file.

1. Create a new file: `staticfiles/css/portfolio.css`
2. Move all your `<style>` contents from `portfolio.html` into this CSS file.

---

### 9.3: Update `portfolio.html` to Use Static File

At the top of your `portfolio.html`, **load the static tag** like this:

```django
{% load static %}
```

Then, link your CSS file:

```html
<link rel="stylesheet" href="{% static 'css/portfolio.css' %}" />
```

---

### 📝 Why `{% load static %}`?

Django doesn’t automatically understand what `{% static %}` means.
You must include `{% load static %}` at the top of any template where you're using the `{% static %}` tag — it's what enables static file linking in templates.

---

✅ Now your CSS is separated, clean, and reusable — and your portfolio page will use it properly!

---

## 🧱 Step 10: Set Up a `base.html` Template

To avoid repeating the same HTML boilerplate across multiple templates, we’ll create a `base.html` layout file. All other templates will then **extend** this base — making your code cleaner and more maintainable.

---

### 🗂️ 10.1: Create `base.html`

Inside the `templates/` directory, create a new file named `base.html`. This file will include all common structure such as:

- `<!DOCTYPE html>`
- `<html>`, `<head>`, and `<body>` tags
- A `{% block content %}{% endblock %}` for dynamic page content
- A `{% block extra_head %}{% endblock %}` for page-specific styles or scripts inside the `<head>`

You don’t need to paste any actual code now — just make sure this structure exists.

---

### 🔄 10.2: Update Templates to Extend the Base

Update templates like `home.html`, `post_list.html`, and `post_detail.html` to use the base layout.

Replace the full HTML structure with:

```django
{% extends 'base.html' %}

{% block content %}
    <!-- Page-specific content goes here -->
{% endblock %}
```

This way, you only define what's unique for each page inside the `{% block content %}` tag.

---

### 🎨 10.3: Customize `portfolio.html`

Some pages, like `portfolio.html`, may include special styles or external resources (e.g. Font Awesome, custom CSS). For those, you can also use the optional `{% block extra_head %}` to include custom code inside the `<head>`:

```django
{% extends 'base.html' %}

{% block extra_head %}
    <!-- Portfolio-specific styles and scripts -->
{% endblock %}

{% block content %}
    <!-- Portfolio content -->
{% endblock %}
```

This gives each page flexibility to inject custom head content without duplicating the full structure.

---

### 🧪 10.4: Test the Pages

Make sure all your templates still load and display content correctly after applying `base.html`. Your pages should look the same but now with a cleaner structure behind the scenes.

---

♻️ **Why this matters:** Using a base template keeps your project **DRY (Don’t Repeat Yourself)** and makes site-wide updates much easier and faster.

---

## 🔐 Step 11: Add User Authentication

Now we’ll allow users to **sign up** on our blog site. For that, we’ll create a new app called `users`, handle user registration, and wire it into the project. Let’s break it down.

---

### 🛠️ 11.1: Create the `users` App

Run the following command to create a new Django app:

```bash
python manage.py startapp users
```

Then, register it in `blog_site/settings.py`:

```python
INSTALLED_APPS = [
    ...
    "posts",
    "users",
]
```

---

### 🌐 11.2: Create a `users/urls.py` File

This file will manage all the URL patterns related to user accounts (signup, login, logout, profile, etc.).

```python
from django.urls import path

from .views import signup_view

urlpatterns = [
    path("signup/", signup_view, name="signup"),
]
```

Don’t forget to include this in `blog_site/urls.py`:

```python
from django.urls import include

urlpatterns = [
    ...
    path("users/", include("users.urls")),
]
```

**Why use `users/urls.py`?**
Separating URLs into different files for each app helps keep our project modular and maintainable. Instead of putting everything in `blog_site/urls.py`, we define user-related URLs inside the `users` app and include them in the main URL configuration.

> 📝 Note: You can also move all post URLs from `blog_site/urls.py` to `posts/urls.py`.

---

### 🧠 11.3: Create the Signup View

Create a view in `users/views.py` to handle registration logic:

```python
from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import SignupForm


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Log the user in
            login(request, user)
            return redirect("home")
    else:
        form = SignupForm()
    return render(request, "signup.html", {"form": form})
```

---

### 🧾 11.4: Create a Custom Signup Form

We'll extend Django’s built-in `UserCreationForm` to include the email field:

```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given username,
    email and password.
    """

    class Meta:
        model = User
        fields = ("username", "email")
```

---

### 🖼️ 11.5: Create the Signup Page Template

Finally, create a `signup.html` file inside your `templates` folder:

```html
{% extends "base.html" %}

{% block content %}
    <h2>Register</h2>

    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Sign Up</button>
    </form>
{% endblock %}
```

---

### 🧩 Extra: Understanding `{% csrf_token %}` and `{{ form.as_p }}`

#### 🔒 `{% csrf_token %}`

This tag adds a **CSRF (Cross-Site Request Forgery) token** to your form.

- It's a security feature built into Django.
- It prevents malicious websites from submitting forms on behalf of your users without their permission.
- Always include this tag inside every form that uses `POST` in Django.

#### 🎨 `{{ form.as_p }}`

This renders the entire Django form as **HTML `<p>` elements**.

- Each field (like username, email, password) will be wrapped in a `<p>` tag.
- It’s a quick way to display all form fields with basic styling.
- You can also use `form.as_table` or `form.as_ul` for different layouts, or render fields manually for full control.

---

You're now all set with a working signup page! ✅ When users sign up, they’ll be automatically logged in and redirected to the homepage.

---

## 🔑 Step 12: Add Login and Logout Functionality

Now that users can sign up, we’ll let them **log in and log out**. Django provides built-in views for these actions, so we can get this working quickly.

---

### 📁 12.1: Configure URLs for Login and Logout

Add the login and logout paths in your `users/urls.py`:

```python
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import signup_view

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
]
```

---

### 🧭 12.2: Set the Login Redirect URL

Tell Django where to send users after login. Add this in `blog_site/settings.py`:

```python
LOGIN_REDIRECT_URL = "home"
```

---

### 🖼️ 12.3: Create the Login Template

Make a `login.html` template inside your templates folder:

```html
{% extends "base.html" %}

{% block content %}
    <h2>Login</h2>

    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Login</button>
    </form>
{% endblock %}
```

---

### 🚪 12.4: Add a Logout Link

Anywhere in `base.html` template, add a logout button:

```html
{% if user.is_authenticated %}
    <p>Hi, {{ user.username }}!</p>
    <form method="post" action="{% url 'logout' %}">
        {% csrf_token %}
        <button type="submit">Logout</button>
    </form>
{% else %}
    <a href="{% url 'login' %}">Login</a>
    <a href="{% url 'signup' %}">Sign Up</a>
{% endif %}
```

---

#### ⚠️ Why Django 5+ Requires POST for Logout

##### 📌 Before

You could log out just by visiting a link like:

```html
<a href="{% url 'logout' %}">Logout</a>
```

This triggered a GET request. The problem?
An attacker could trick a user into clicking a hidden link and log them out without consent.

---

##### ✅ Now (Django 5+)

To avoid this, Django requires **logout to be triggered via POST**, which can't be done just by clicking a link — it needs a deliberate action (like submitting a form).

---

##### ✅ How to Do It Properly

Use a form with a POST method and CSRF protection:

```html
<form method="post" action="{% url 'logout' %}">
    {% csrf_token %}
    <button type="submit">Logout</button>
</form>
```

This ensures:

- The user **intentionally** logs out.
- CSRF protection is enforced.
- You're following **Django’s secure default behavior**.

---

You now have working **login and logout functionality** 🎉
