
# 📦 Project Setup and Final Submission Guide

---

## 🧩 1. Install Homebrew (Mac Only)

> Skip this step if you're on Windows.

Homebrew is a package manager for macOS.  
You’ll use it to easily install Git, Python, Docker, etc.

### Install Homebrew:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Verify Homebrew:

```bash
brew --version
```

If you see a version number, you're good to go.

---

## 🧩 2. Install and Configure Git

### Install Git

- **MacOS (using Homebrew)**

```bash
brew install git
```

- **Windows**

Download and install [Git for Windows](https://git-scm.com/download/win).  
Accept the default options during installation.

### Verify Git:

```bash
git --version
```

---

### Configure Git Globals

Set your name and email so Git tracks your commits properly:

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

Confirm the settings:

```bash
git config --list
```

---

### Generate SSH Keys and Connect to GitHub

> Only do this once per machine.

1. Generate a new SSH key:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

(Press Enter at all prompts.)

2. Start the SSH agent:

```bash
eval "$(ssh-agent -s)"
```

3. Add the SSH private key to the agent:

```bash
ssh-add ~/.ssh/id_ed25519
```

4. Copy your SSH public key:

- **Mac/Linux:**

```bash
cat ~/.ssh/id_ed25519.pub | pbcopy
```

- **Windows (Git Bash):**

```bash
cat ~/.ssh/id_ed25519.pub | clip
```

5. Add the key to your GitHub account:
   - Go to [GitHub SSH Settings](https://github.com/settings/keys)
   - Click **New SSH Key**, paste the key, save.

6. Test the connection:

```bash
ssh -T git@github.com
```

You should see a success message.

---

## 🧩 3. Clone the Repository

Now you can safely clone the course project:

```bash
git clone <repository-url>
cd <repository-directory>
```

---

## 🛠️ 4. Install Python 3.10+

### Install Python

- **MacOS (Homebrew)**

```bash
brew install python
```

- **Windows**

Download and install [Python for Windows](https://www.python.org/downloads/).  
✅ Make sure you **check the box** `Add Python to PATH` during setup.

### Verify Python:

```bash
python3 --version
```
or
```bash
python --version
```

---

## 🛠️ 5. Create and Activate a Virtual Environment

(Optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate.bat  # Windows
```

### Install Required Packages

```bash
pip install -r requirements.txt
```

---

## 🐳 6. (Optional) Docker Setup

> Skip if Docker isn't used in this module.

### Install Docker

- [Install Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/)
- [Install Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/)

### Build Docker Image

```bash
docker build -t fastapi-calculator .
```

### Run Docker Container

```bash
docker run -it --rm -p 8000:8000 fastapi-calculator
```

---

## 🚀 7. Running the Project

- **Without Docker**:

```bash
python main.py
```

- **With Docker**:

```bash
docker run -it --rm -p 8000:8000 fastapi-calculator
```

Visit `http://localhost:8000` in your browser.

---

## ✅ 8. Final Enhancements and Test Coverage

This project includes full-stack testing and validation across three layers:

---

### 🔍 Unit Tests

- Located in `tests/unit/test_calculator.py`
- Covers all arithmetic functions: `add`, `subtract`, `multiply`, `divide`
- Includes edge cases:
  - Negative numbers
  - Floating-point precision
  - Division by zero
- ✅ Achieved **100% test coverage** of `app/operations/__init__.py`

---

### 🔗 Integration Tests

- Located in `tests/integration/test_fastapi_calculator.py`
- Tests all API endpoints:
  - `/add`, `/subtract`, `/multiply`, `/divide`
- Validates:
  - Correct status codes (`200`, `400`)
  - JSON response structure and values
  - Error handling for divide-by-zero and invalid input
- ✅ Fixed mismatch in `test_invalid_input_api` to expect `400` instead of `422`

---

### 🌐 End-to-End (E2E) Tests

- Located in `tests/e2e/test_e2e.py`
- Uses Playwright to simulate real user interactions in the browser
- Tests include:
  - Homepage rendering (`Hello World`)
  - All calculator operations via UI
  - Divide-by-zero error handling
  - Invalid input handling using JavaScript injection to bypass `type="number"` restriction
- ✅ Fixed `test_calculator_divide` to accept both `"5"` and `"5.0"` formatting

---

### 🧪 Test Summary

| Layer         | File Location                                | Status         |
|---------------|-----------------------------------------------|----------------|
| Unit Tests    | `tests/unit/test_calculator.py`               | ✅ All passed   |
| Integration   | `tests/integration/test_fastapi_calculator.py`| ✅ All passed   |
| End-to-End    | `tests/e2e/test_e2e.py`                        | ✅ All passed   |
| Coverage      | `app/operations/__init__.py`                  | ✅ 100%         |

---

## 📊 9. Run Tests and View Coverage

### Run All Tests

```bash
pytest
```

### Run with Coverage Report

```bash
pytest --cov=app
```

### Generate HTML Coverage Report

```bash
pytest --cov=app --cov-report=html
```

Then open `htmlcov/index.html` in your browser.

---

## 🧪 10. GitHub Actions (CI/CD)

This project includes a GitHub Actions workflow that:

- Installs dependencies
- Runs all tests
- Fails the build if any test fails
- Ensures code quality and reproducibility

✅ All tests pass in CI  
✅ GitHub Actions badge (optional) can be added to README

---

## 📝 11. Submission Instructions

After finishing your work:

```bash
git add .
git commit -m "Final test suite: 100% coverage, all tests passing"
git push origin main
```

Then submit your GitHub repository link as instructed.

---

## 🔥 12. Useful Commands Cheat Sheet

| Action                         | Command                                          |
|-------------------------------|--------------------------------------------------|
| Install Git                   | `brew install git` or Git for Windows installer |
| Configure Git Username        | `git config --global user.name "Your Name"`     |
| Configure Git Email           | `git config --global user.email "you@example.com"` |
| Clone Repository              | `git clone <repo-url>`                          |
| Create Virtual Environment    | `python3 -m venv venv`                           |
| Activate Virtual Environment  | `source venv/bin/activate` / `venv\Scripts\activate.bat` |
| Install Python Packages       | `pip install -r requirements.txt`               |
| Run Project                   | `python main.py`                                 |
| Run Tests                     | `pytest`                                         |
| Run Tests with Coverage       | `pytest --cov=app`                               |
| View HTML Coverage Report     | `pytest --cov=app --cov-report=html`            |
| Build Docker Image            | `docker build -t fastapi-calculator .`          |
| Run Docker Container          | `docker run -it --rm -p 8000:8000 fastapi-calculator` |
| Push Code to GitHub           | `git add . && git commit -m "message" && git push` |

---

## 📎 Quick Links

- [Homebrew](https://brew.sh/)
- [Git Downloads](https://git-scm.com/downloads)
- [Python Downloads](https://www.python.org/downloads/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [GitHub SSH Setup Guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
- [Playwright Testing Docs](https://playwright.dev/python/docs/intro)
- [FastAPI Docs](https://fastapi.tiangolo.com/)

---

## 📋 Notes

- Use Python 3.10+ and virtual environments for clean dependency management.
- Docker is optional but useful for containerized deployment.
- GitHub Actions ensures your code is always tested before merging or deploying.
- All tests are designed to be reproducible and reflect real-world usage.

---



