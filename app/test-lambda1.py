from functools import reduce


def checkLambda1():
    double = lambda x: x * 2
    print(double(5))
    
    # Example use with filter()  
    my_list = [1, 5, 4, 6, 8, 11, 3, 12]
    new_list = list(filter(lambda x: (x % 2 == 0) , my_list))
    print(new_list)  # [4, 6, 8, 12]
    
    # Example use with map()
    my_list = [1, 5, 4, 6, 8, 11, 3, 12]
    new_list = list(map(lambda x: x * 2 , my_list))
    print(new_list)  # [2, 10, 8, 12, 16, 22, 6, 24]

    
def sumOfAllNo():
    li = [5, 8, 10, 20, 50, 100] 
    sum = reduce((lambda x, y: x + y), li) 
    print (sum) # 193

    
if __name__ == "__main__":
    checkLambda1()  # 10 
    sumOfAllNo()
    
