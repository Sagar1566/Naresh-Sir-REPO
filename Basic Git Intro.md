# Git & GitHub Basics

This document explains the basics of **Git**, **repositories**, and **GitHub** in a simple and beginner-friendly way.

---

## What is Git?

**Git** is a **version control system** used to track changes in files and source code.

It helps developers to:
- Track changes in code
- Revert to previous versions
- Work on features safely
- Collaborate with others

Git works locally on your system.

---

## What is a Repository (Repo)?

A **repository** is a project folder that is tracked by Git.

It contains:
- Project files (code, images, documents)
- A hidden `.git` folder that stores commit history

---

## How to Create a Git Repository (Local)

Follow these steps to create a local Git repository:

```bash
cd your-project-folder
git init
````

This initializes Git in your project directory.

---

## Common Git Commands

### Basic Commands

| Command                   | Description                     |
| ------------------------- | ------------------------------- |
| `git init`                | Initialize a new Git repository |
| `git status`              | Check the status of files       |
| `git add .`               | Add all files to staging area   |
| `git add <file>`          | Add a specific file             |
| `git commit -m "message"` | Save changes with a message     |
| `git log`                 | View commit history             |
| `git diff`                | View changes between commits    |

---

### Branching Commands

| Command                  | Description              |
| ------------------------ | ------------------------ |
| `git branch`             | List branches            |
| `git branch <name>`      | Create a new branch      |
| `git checkout <name>`    | Switch branch            |
| `git checkout -b <name>` | Create and switch branch |
| `git merge <branch>`     | Merge a branch           |

---

### Remote Repository Commands

| Command                       | Description               |
| ----------------------------- | ------------------------- |
| `git remote add origin <url>` | Connect GitHub repository |
| `git push origin main`        | Push code to GitHub       |
| `git pull origin main`        | Pull updates from GitHub  |
| `git clone <url>`             | Clone a repository        |

---

## What is GitHub?

**GitHub** is a cloud-based platform that hosts Git repositories.

It allows developers to:

* Store code online
* Collaborate with teams
* Track issues
* Showcase projects

GitHub uses Git for version control.

---

## How to Create a Repository on GitHub

1. Go to [https://github.com](https://github.com)
2. Log in to your account
3. Click **New Repository**
4. Enter repository name and details
5. Choose **Public** or **Private**
6. Click **Create repository**

---

## Push Local Repository to GitHub

```bash
git remote add origin https://github.com/username/repository-name.git
git branch -M main
git push -u origin main
```

---

## Summary

* **Git** tracks changes in code
* **Repository** stores project and history
* **GitHub** hosts repositories online
* Git helps developers collaborate efficiently

---

Happy Coding 🚀

## Screenshots

### Account Image
![Account Image](image.png)

### Demo Image
![Demo Image](image%20copy.png)
