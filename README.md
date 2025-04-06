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
