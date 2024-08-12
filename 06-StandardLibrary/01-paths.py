from pathlib import Path

# use a "raw string" use r
# Path(r"C:\Program Files\Microsoft")
# Path("/usr/local/bin")
# Path()
# Path("ecommerce/__init__.py")
# Path() / Path("ecommerce")  # combine
# Path() / "ecommerce" / "__init__.py" #combine with strings
# Path.home()  # get home directory of current user

path = Path("ecommerce/__init__.py")
print(path)
print(path.exists())
print(path.is_file())
path.is_dir()
print(path.name)  # __init__.py
print(path.stem)  # file name without the extension
print(path.suffix)  # get the file extension
print(path.parent)  # returns the parent folder

# create a new path object based on existing path bubt only change the name and the extension of the file.
# path = path.with_name("file.txt")
# print(path)  # ecommerce\file.txt
# print(path.absolute())  # absolute path. C:\Demos\Python\mosh\ecommerce\file.txt

path = path.with_suffix(".txt")  # we use it to change the extension of a file
print(path)  # we are not renaming, only representing a path object.
