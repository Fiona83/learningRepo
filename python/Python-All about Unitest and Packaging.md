# Python Unittest

The purpose of the **unittest** is to check if the functions working properly, does what it should do. 
Therefore we right a test file with multiple test cases in it to verify the functionality of the functions.

In the path of the software development, after we wrote the functions or modules with multiple functions in it. The first thing to do is do the **unittest**.
After the code pass the unittest, we send it then to the CI/CD server to test it. 
If it also passes the server test, we can now merge the code into the master branch and deploy it.

## How does unittest work?
Now we will explain how does the unitest work with the following example.

Assume we have developed a module named ***mymodule.py***. Within the module, we have defined multiple functions as follows:

```python
# mymodule.py

def add(n1, n2):
  return n1 + n2
  
def double(n1):
  return n1 * 2
```

Then to make a unittest on this module, we define a test file named ***test_mymodule.py***. 
1. First thing to do is to import the unittest.
2. Import the function from the module
3. Define a class for the test cases.
4. Run the test in main function.

Following is the example:

```python
# test_mymodule.py

import unittest
from mymodule import add, double

class TestMyModule(unittest.TestCase):
  def test_add(self):
    self.assertEqual(add(2, 3), 5)
    self.assertEqual(add(0, 1), 1)
    self.assertNotEqual(add(2, 2), 0)
   
  def test_double(self):
    self.assertEqual(double(0), 0)
    self.assertEqual(double(2), 4)

if __name__ = '__main__':
  unittest.main()

```

# Python Packaging

Packaging is to package multiple modules into one big package.
1. All the modules of the package should be placed in one folder.
2. Create a ***\_\_init\_\_.py***, within the file we should import all the modules as follows:

```python
from . import module1
from . import module2
```

3. To use the functions in the package, we can import the whole package and call the function as follows:

```python
import package
# call the function
package.module1.function1()
```

or we can import the functions as follows:

```python
from package.module1 import function1, function2
from package.module2 import function3, function4
# call the function
function1()
function2()
```
