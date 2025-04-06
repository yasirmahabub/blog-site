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

```
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
