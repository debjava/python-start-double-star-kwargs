'''
Created on Oct 11, 2020

@author: debad
'''
#  pass key value as variable argument


def showKeyAndValue(**kwargs):
    for key, value in kwargs.items():
        print(key , "<--->" , value)


def showKeyValueFromObject(**kwargs):
    for key, value in kwargs.items():
        print ("%s == %s" % (key, value))

        
def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)


if __name__ == '__main__':
    showKeyAndValue(name = "DD", age = 27, desgn = "Architect")
    obj = {"name" : "DD", "age" : 27, "desgn" : "Architect"}
    showKeyValueFromObject(**obj)
    myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")
