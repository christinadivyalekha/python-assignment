import os
myfile="/tmp/foo.txt"


if os.path.isfile(myfile):
    os.remove(myfile)
else:    
    print("Error: %s file not found" % myfile)
