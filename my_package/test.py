# You can use relative imports
# Run as
# python -m my_package.test
# (*not* as python -m my_package.test.py)
# from directory above this one
#
from . import module_A, module_B

print(module_A.hello())  
print(module_B.bye())    
