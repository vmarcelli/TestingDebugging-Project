## This version of Pagan is a testing project by CPSC 5210, Group 4
### Valerio Marcelli, Alberto Valdiviez, Helena Taflin
pagan
=====

Welcome to the Python Avatar Generator for Absolute Nerds.

**Current version: 0.4.3**

View the change history [here](CHANGELOG.md).
 

**Pagan is currently under development. It can perform the following functions:**

* Generate identicons with unique colors and gear based on any input string.
* Use multiple hash functions from within Python's hashlib.
* Create avatar images to fit a specific resolution.
* Remap 16x16 generated pixelmaps to a required image size.
* Expand generated pagans by adding new weapons or gear.


#

### Installation:
#### Python
You will need Python.  
Pagan works with any 3.x version of **Python**.
The first step is to get a functioning Python environment set-up before starting anything.  
For the purpose of this tutorial we will be using [Anaconda 3](https://www.anaconda.com/distribution/) as our Python tool of choice.

#### Pytest
The first thing you will need to run tests, will be to install **pytest**.  
To do install pytest, open up your **Anaconda Prompt** (search for it through your start menu if on windows)  
Then type:
```
>> conda install pytest
```
That's it! That should get you set up with pytest! 

#### Pagan
To install Pagan, first clone this repository:
```
>> git clone https://github.com/vmarcelli/TestingDebugging-Project.git
```
Then, enter this command at the terminal to manually install Pagan:
```
>> python setup.py install
```
Alternatively, use this command to install pagan in your **Anaconda Prompt**:
```
>> pip install pagan
```

### Testing Pagan:
First make sure that you are in the directory where you downloaded pagan.  
You should be in the 'TestingDebugging-Project' folder
In your Anaconda Prompt simply type in:
```
>> pytest
```
This will run the unit tests inside of the 'test' folder.
 
#


### Python usage example:
```python
# Import the pagan module.
import pagan

# Acquire an arbitrary string.
inpt = 'pagan'

# Use pagan to generate an avatar object based on an input string.
# Optional: You may specify which hash function Pagan should use.
# The functions are available as constants.
# Default: MD5.
img = pagan.Avatar(inpt, pagan.SHA512)

# Open the avatar image in an
# external image viewer.
img.show()

# Set an output path and a file name.
# You don't need to specify a file ending.
# Choose a path depending on your OS.
outpath = 'output/'
filename = inpt

# Saves the avatar image as a .png file
# by omitting the path and name. The
# file endings will be generated automatically.
img.save(outpath, filename)

# You can change the avatar input and
# hash function anytime.
img.change('new input', pagan.SHA256)
```

### Supported Hashes

Hash     | Constant
-------- | --------
md5 | pagan.MD5
sha1 | pagan.SHA1
sha224 | pagan.SHA224
sha256 | pagan.SHA256
sha384 | pagan.SHA384
sha512 | pagan.SHA512
