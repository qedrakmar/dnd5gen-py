import sys
a = ['apple', 'banana', 'cherry', 'durian']

b={'apple':'starts with a','banana':'with b','cherry':'a c','durian':'stinky'}

# for i in range(4):
#     j = a[i]
#    $j()  doesn't work
#    print b[j]

#def fruit(*args):
#    &args()

#fruit(a)
def apple():
    print "apple"
def banana():
    print "b"
def cherry():
    print "c"
def durian():
    print "d"

for item in a:
    getattr(sys.modules[__name__],item)()
#    eval(item)()
    


