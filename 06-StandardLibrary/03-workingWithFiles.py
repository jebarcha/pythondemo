from pathlib import Path
from time import ctime
import shutil

source = Path("ecommerce/__init__.py")
target = Path() / "__init__.py"

# target.write_test(source.read_text())
shutil.copy(source, target)  # easier and clener approach using shutil


# path = Path("ecommerce/__init__.py")
# path.exists()
# path.rename("init.txt")
# path.unlink()

# print(path.stat())
# print(ctime(path.stat().st_ctime))  # creation time of a file

# with open("__init__.py", "r") as file:
#   ...

# instead we can use the read_text:
# path.read_bytes()
# print(path.read_text())
# all these methods take care of opening and closing the file
# path.write_test("...")
# path.write_bytes()

# however when copying a file, the path object is not the ideal way
