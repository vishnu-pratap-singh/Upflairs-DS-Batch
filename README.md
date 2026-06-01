# Upflairs-DATA SCIENCE-Internship
Data Science and AI and ML intership 
# Connecting GitHub with VS Code: Step-by-Step Guide

This guide walks you through setting up a secure connection between Visual Studio Code (VS Code) and your GitHub account so you can seamlessly push, pull, and manage your Data Science project files.

---

## 🛠️ Prerequisites
Before starting, make sure you have installed:
1. **Git** installed on your local machine ([Download Git](https://git-scm.com/))
2. **VS Code** installed ([Download VS Code](https://code.visualstudio.com/))
3. A registered **GitHub account**

---

## 🚀 The Setup Process

### Step 1: Configure Git Globally
Open your terminal (or Git Bash on Windows) and introduce yourself to Git. This ensures your commits are linked to your GitHub profile.

```bash
git config --global user.name "Your GitHub Username"
git config --global user.email "your_email@example.com"

🔄 Daily Workflow (Save & Push Your Work)
Whenever you add new Jupyter Notebooks, datasets, or scripts, use this standard sequence in the VS Code Source Control panel (Ctrl + Shift + G):

Stage Changes (git add): Hover over the changed files and click the + icon to stage them.

Commit (git commit): Type a clear descriptive message in the text box (e.g., "Added Week 1 Python basics notebook") and click the Commit button.

Push (git push): Click the Sync Changes button (or the ... icon -> Push) to send your code to GitHub.
