from MainPackage import mainpackage
# from MainPackage.SubPackage import subpackage

def somerandomapp():
    print ("we're now in a caller app")


somerandomapp()
print("But now we're in:")
mainpackage.main_func()