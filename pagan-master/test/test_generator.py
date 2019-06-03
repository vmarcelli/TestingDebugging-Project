'''
  _    _ _   _ _      ______  _____ _____  __     ______  _    _ _____    _   _          __  __ ______    
 | |  | | \ | | |    |  ____|/ ____/ ____| \ \   / / __ \| |  | |  __ \  | \ | |   /\   |  \/  |  ____|   
 | |  | |  \| | |    | |__  | (___| (___    \ \_/ / |  | | |  | | |__) | |  \| |  /  \  | \  / | |__      
 | |  | | . ` | |    |  __|  \___ \\___ \    \   /| |  | | |  | |  _  /  | . ` | / /\ \ | |\/| |  __|     
 | |__| | |\  | |____| |____ ____) |___) |    | | | |__| | |__| | | \ \  | |\  |/ ____ \| |  | | |____    
  \____/|_|_\_|______|______|_____/_____/___ _|_|_ \____/ \____/|_|  \_\ |_| \_/_/    \_\_|  |_|______|   
 |_   _|/ ____| \ \    / /\   | |    |  ____|  __ \|_   _/ __ \                                           
   | | | (___    \ \  / /  \  | |    | |__  | |__) | | || |  | |                                          
   | |  \___ \    \ \/ / /\ \ | |    |  __| |  _  /  | || |  | |                                          
  _| |_ ____) |    \  / ____ \| |____| |____| | \ \ _| || |__| |                                          
 |_____|_____/    _ \/_/ ___\_\______|______|_| _\_\_____\____/____ _    _   _______ _    _ _____  _____  
 |  __ \ / __ \  | \ | |/ __ \__   __| |__   __/ __ \| |  | |/ ____| |  | | |__   __| |  | |_   _|/ ____| 
 | |  | | |  | | |  \| | |  | | | |       | | | |  | | |  | | |    | |__| |    | |  | |__| | | | | (___   
 | |  | | |  | | | . ` | |  | | | |       | | | |  | | |  | | |    |  __  |    | |  |  __  | | |  \___ \  
 | |__| | |__| | | |\  | |__| | | |       | | | |__| | |__| | |____| |  | |    | |  | |  | |_| |_ ____) | 
 |_____/ \____/  |_|_\_|\____/__|_|   _  _|_|_ \____/_\____/ \_____|_|__|_|    |_|  |_|  |_|_____|_____/  
 |  ____| |  | |/ ____| |/ /_   _| \ | |/ ____|  / ____/ __ \|  __ \|  ____|                              
 | |__  | |  | | |    | ' /  | | |  \| | |  __  | |   | |  | | |  | | |__                                 
 |  __| | |  | | |    |  <   | | | . ` | | |_ | | |   | |  | | |  | |  __|                                
 | |    | |__| | |____| . \ _| |_| |\  | |__| | | |___| |__| | |__| | |____                               
 |_|     \____/ \_____|_|\_\_____|_| \_|\_____|  \_____\____/|_____/|______|                              
 
'''
import pagan
import pytest
import sys
import os

def generator_MD5():
    print()

def test_hashGen():
    import hashlib
    md5 = hashlib.md5()
    input = ""

    #Check for version issues
    if(sys.version_info.major == 2):
        input = bytes(input)
    else:
        input = bytes(input, "utf-8")

    #Update the Hashcode with the input
    #Generate the image using hash
    md5.update(input)
    imgOne = pagan.generator.generate_by_hash(md5.hexdigest())
    imgTwo = pagan.generator.generate("", 0) #Default generator is md5
    assert (imgOne is not None)
    assert (imgOne == imgTwo)

    #Pytest Errors
    with pytest.raises(pagan.generator.FalseHashError):
        imgOne = pagan.generator.generate_by_hash(md5.hexdigest()[:2])
    with pytest.raises(pagan.generator.FalseHashError):
        imgOne = pagan.generator.generate_by_hash(md5.hexdigest()+"A")

    #Test Globals
    assert pagan.generator.OUTPUT_PATH == ('%s%soutput%s' % (os.getcwd(), os.sep, os.sep))
