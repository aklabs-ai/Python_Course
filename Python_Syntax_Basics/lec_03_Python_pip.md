# Python pip — Complete Notes

## 1. What is pip?

**pip** stands for **"Pip Installs Packages"** (a recursive acronym). It is Python's standard **package manager**, used to install, upgrade, and remove third-party libraries/packages that are not part of the Python standard library.

Packages are hosted on **PyPI** — the **Python Package Index** (https://pypi.org) — a huge public repository of Python packages.

**Why use pip?**
- Access thousands of ready-made libraries (e.g., `numpy`, `pandas`, `requests`, `flask`, `django`) instead of writing everything from scratch.
- Easily manage versions of packages.
- Share your own packages with others.
- Automatically handle **dependencies** (packages that your package depends on).

---

## 2. Checking if pip is Installed

Pip usually comes pre-installed with Python (from Python 3.4+). To check:

```bash
pip --version
```

or, if you have multiple Python versions:

```bash
python -m pip --version
python3 -m pip --version
```

**Explanation:** This prints the pip version along with the Python version and path it's linked to, confirming pip is available and which Python installation it manages.

---

## 3. Installing a Package

```bash
pip install package_name
```

**Example:**
```bash
pip install requests
```

**Explanation:** This downloads the `requests` package (and any dependencies) from PyPI and installs it into your current Python environment, making it available for `import requests` in your scripts.

### Installing a specific version
```bash
pip install requests==2.28.0
```

### Installing a minimum version
```bash
pip install requests>=2.25.0
```

**Explanation:** The `==` pins an exact version; `>=` allows any version equal to or newer than specified. This is useful to avoid compatibility issues when a package updates and breaks old code.

---

## 4. Upgrading a Package

```bash
pip install --upgrade package_name
```

**Example:**
```bash
pip install --upgrade requests
```

**Explanation:** This fetches the latest version of `requests` from PyPI and replaces the currently installed version.

---

## 5. Uninstalling a Package

```bash
pip uninstall package_name
```

**Example:**
```bash
pip uninstall requests
```

**Explanation:** pip will ask for confirmation (`y/n`) before removing the package files from your environment.

---

## 6. Listing Installed Packages

```bash
pip list
```

**Explanation:** Shows all packages currently installed in the active Python environment, along with their versions.

To check details of one specific package:
```bash
pip show requests
```

**Explanation:** Displays metadata like version, summary, home page, author, license, and dependencies (`Requires:`) for that package.

---

## 7. Checking for Outdated Packages

```bash
pip list --outdated
```

**Explanation:** Lists packages that have newer versions available on PyPI than what's currently installed.

---

## 8. Freezing Requirements (Exporting Installed Packages)

```bash
pip freeze > requirements.txt
```

**Explanation:** This writes all currently installed packages (with exact versions) into a file called `requirements.txt`. This file is commonly shared with a project so others can replicate the exact same environment.

### Installing from a requirements file
```bash
pip install -r requirements.txt
```

**Explanation:** Reads the `requirements.txt` file line by line and installs each listed package with its specified version — extremely useful for setting up a project on a new machine.

---

## 9. Virtual Environments (Best Practice with pip)

It's best practice to install packages inside a **virtual environment** rather than globally, so different projects don't conflict with each other's dependencies.

```bash
python -m venv myenv          # create a virtual environment named "myenv"

# Activate it:
# On Windows:
myenv\Scripts\activate
# On macOS/Linux:
source myenv/bin/activate

pip install requests          # now installs only inside myenv

deactivate                    # exit the virtual environment
```

**Explanation:** A virtual environment is an isolated Python setup. Packages installed while it's activated don't affect your global Python installation or other projects — keeping dependencies clean and project-specific.

---

## 10. Upgrading pip Itself

```bash
python -m pip install --upgrade pip
```

**Explanation:** pip itself is a package and can be outdated; this command updates pip to its latest version.

---

## Examples with Solutions & Explanations

### Example 1: Installing and using a package
**Problem:** Install the `requests` package and use it to fetch data from a website.

**Step 1 — Install:**
```bash
pip install requests
```

**Step 2 — Use it in Python:**
```python
import requests

response = requests.get("https://api.github.com")
print("Status Code:", response.status_code)
print("Content Type:", response.headers["Content-Type"])
```

**Explanation:** After installing via pip, `requests` becomes importable. `requests.get()` sends an HTTP GET request, and `response.status_code` / `response.headers` let us inspect the server's response.

---

### Example 2: Checking installed package version
**Problem:** Check which version of `numpy` (if any) is installed, and get details about it.

```bash
pip show numpy
```

**Sample Output:**
```
Name: numpy
Version: 1.26.4
Summary: Fundamental package for array computing in Python
...
```

**Explanation:** `pip show` reveals metadata without needing to open Python — useful for quickly verifying compatibility before writing code that depends on a specific version.

---

### Example 3: Creating a requirements.txt for a project
**Problem:** You've installed `flask` and `requests` for a small web project. Create a file that lists these dependencies for teammates.

```bash
pip freeze > requirements.txt
```

**Sample `requirements.txt` content:**
```
Flask==3.0.0
requests==2.31.0
```

**Explanation:** Anyone who clones your project can now run `pip install -r requirements.txt` to install the exact same package versions, ensuring the project behaves consistently across machines.

---

### Example 4: Uninstalling an unused package
**Problem:** You installed `pandas` for testing but no longer need it. Remove it.

```bash
pip uninstall pandas
```

**Sample interaction:**
```
Found existing installation: pandas 2.1.4
Uninstalling pandas-2.1.4:
  Would remove:
    ...
Proceed (y/n)? y
  Successfully uninstalled pandas-2.1.4
```

**Explanation:** Confirming with `y` removes all files associated with `pandas` from the current Python environment, freeing up space and keeping the environment clean.

---

### Example 5: Using a virtual environment with pip
**Problem:** Set up an isolated environment for a project that needs `django`, without affecting your global Python setup.

```bash
python -m venv projectenv
source projectenv/bin/activate      # macOS/Linux
pip install django
python -m django --version
deactivate
```

**Explanation:** `venv` creates a self-contained folder (`projectenv`) with its own Python interpreter and `site-packages`. Activating it redirects `pip install` to that isolated location. `deactivate` returns you to the global environment, leaving your system Python untouched.

---

## Extra Practice Questions

1. Check which version of pip is installed on your system.
2. Install the `colorama` package and write a small script that prints colored text using it.
3. Use `pip show` to check details about the `setuptools` package.
4. Upgrade the `requests` package to its latest version (or reinstall if already latest, and note the output).
5. List all currently installed packages in your environment using `pip list`.
6. Create a virtual environment named `testenv`, activate it, install `beautifulsoup4`, then deactivate and verify (via `pip list`) that it's not installed globally.
7. Generate a `requirements.txt` file for your current environment using `pip freeze`.
8. Write down the difference between `pip install package` and `pip install package==1.0.0` — when would you use each?
9. Simulate a fresh project setup: create a `requirements.txt` manually with 2 package names and versions, then install from it using `pip install -r requirements.txt`.
10. Research and write (in a comment) what `pip install --user package_name` does differently compared to a normal `pip install`.

---

*Type the next topic name, or type **stop** to end.*
