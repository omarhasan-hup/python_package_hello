
# Python Packaging Summary

## Purpose of Python Packaging

The goal of Python packaging is to promote code reusability and distribution by wrapping your code in a standardized format that others (or you) can install using `pip`.

---

## Distribution Types

There are two main types of Python distributions built using `setuptools` and optionally `wheel`:

### 1. Source Distribution (sdist)
- Format: `.tar.gz`
- Contains: Raw Python source code
- Built with: `python setup.py sdist`
- Note: Must be built/compiled at install time

### 2. Binary Distribution (Wheel)
- Format: `.whl`
- Contains: Pre-built code (source or compiled)
- Built with: `python setup.py bdist_wheel`
- Note: Faster to install (no build step)

---

## Tooling

- `setuptools`: The main tool to describe and build the package using `setup.py`.
- `wheel`: Adds support for building `.whl` files.
- Essential `setup.py` Keys:
  - `name`, `version`, `packages=find_packages()`
  - `entry_points` (optional, for CLI tools via `console_scripts`)

---

## Package Structure

- Packages can contain submodules (folders) like `hello/` or `another_hi/`.
- Each module must have an `__init__.py` to be recognized as a valid Python package.

---

## Exposing Functions

- To make your package user-friendly via:
  ```python
  import hello
  hello.main()
  ```
  You must expose functions in `__init__.py` like:
  ```python
  from .hello import main
  ```

---

## Summary Table

| Feature                          | sdist (`.tar.gz`)                | bdist_wheel (`.whl`)           |
|----------------------------------|----------------------------------|--------------------------------|
| Built with                       | `python setup.py sdist`          | `python setup.py bdist_wheel` |
| Contains                         | Source code                      | Pre-built code                 |
| Speed of install                 | Slower (builds on install)       | Fast (just unzip and link)    |
| Requires build tools             | Yes                              | No                             |
| Good for                         | Source distribution & flexibility| Speed and deployment           |

---

## Key Notes

- Always use `console_scripts` in `entry_points` to create CLI commands.
- Re-version your package (`version='0.1.1'`) when making meaningful changes.
- Use `--force-reinstall` if installing the same version again.
- Packages live in `site-packages/` once installed, and can be imported globally.
- We could list all the Packages installed in our Python environmnet by pip using the commnad : `pip list`
