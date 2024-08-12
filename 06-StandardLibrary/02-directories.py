from pathlib import Path

path = Path('ecommerce')
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")

# print(path.iterdir())  # get the list of files and directories in this path.
# returns <generator object Path.iterdir at 0x000001BDAE393780>
# a generator object returns a new value every time we iterate it.
# when we are working with a large list of items, instead of storing all in memory, we use a generator object.
# means we iterate it and get a new value everytime, this is more efficient.

# for p in path.iterdir():
#     print(p)

# if we are not working with a large list, we can convert this to a comprehension expression
# paths = [p for p in path.iterdir()]
# print(paths)

# paths = [p for p in path.iterdir() if p.is_dir()]
# print(paths) # [WindowsPath('ecommerce/customer'), WindowsPath('ecommerce/shopping')]
# limitations are that we cannot search by pattern and recursively
# for those scenarios we can use another method: glob

# *** search by pattern ***
# paths = [p for p in path.iterdir() if p.is_dir()]
# py_files = [p for p in path.glob("*.py")]
# print(py_files)  # [WindowsPath('ecommerce/__init__.py')]

# *** search recursevly ***
# to search recursevly
paths = [p for p in path.iterdir() if p.is_dir()]
# py_files = [p for p in path.glob("**/*.py")]  # with **/*.py
py_files = [p for p in path.rglob("*.py")]  # or use the rglob method
print(py_files)  # [WindowsPath('ecommerce/__init__.py')]
