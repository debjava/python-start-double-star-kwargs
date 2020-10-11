def test1():
    a = 2 * 5
    print("a: ", a)
    b = 2 ** 6
    print("b: ", b)

    
def showAllNums():
    numbers = [2, 1, 3, 4, 7]
    more_numbers = [*numbers, 11, 18]
    print(*more_numbers, sep="\t")

    
def unpackAll():
    fruits = ['lemon', 'pear', 'watermelon', 'tomato']
    print(*fruits)

    
def useDoubleStar1():
    date_info = {'year': "2020", 'month': "01", 'day': "01"}
    filename = "{year}-{month}-{day}.txt".format(**date_info)
    print("File Name: ", filename)

    
def useDoubleStar2():
    fruits = ['lemon', 'pear', 'watermelon', 'tomato']
    numbers = [2, 1, 3, 4, 7]
    print(*numbers, *fruits)

    
def variableAgruments(*dice):
    for die in dice:
        print("Value of die: ", die)

        
def foo(*args):
    for a in args:
        print(a) 

        
def passAsDictionary(**values):
    print("All values: ", values)
    for key, value in values:
        print(key + "---" + value)


def bar(**kwargs):
    for a in kwargs:
        print(a, kwargs[a])

    
if __name__ == "__main__":
    bar(name='one', age=27)
#     foo(1, 2, 3, 4, 5)
#     myDict = {"key-1": "Value-1", "Key-2": "Value-2", "Key-3": "Value-3"}
#     passAsDictionary(**myDict)
#     variableAgruments(5,7,9);
#     useDoubleStar2()
#     useDoubleStar1()
#     test1()
#     showAllNums()
#         unpackAll()
