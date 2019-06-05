'''
Please run this build script file from inside of the test folder in
pagan-master/test

It should set up the pagan dependencies and install pytest for you
ONLY RUN THIS FROM AN ANACONDA 3 SHELL 
If you need instructions on how to use Anaconda see the README.md provided
to get set up

'''

import os
os.chdir(path="../")
os.system("python setup.py install")
os.system("conda install pytest")