import timeit

# def partition(arr, low, high):
#     i = (low-1)         # index of smaller element
#     pivot = arr[high]     
 
#     for j in range(low, high):
 
        
#         if arr[j] <= pivot:
 
            
#             i = i+1
#             arr[i], arr[j] = arr[j], arr[i]
 
#     arr[i+1], arr[high] = arr[high], arr[i+1]
#     return (i+1)
 

 
# def quickSort(arr, low, high):
#     if len(arr) == 1:
#         return arr
#     if low < high:

#         pi = partition(arr, low, high)
 
#         quickSort(arr, low, pi-1)
#         quickSort(arr, pi+1, high)

# numbers=[5,25,1,3,200]  
# n=len(numbers)    
# time=timeit.timeit(quickSort(numbers,0,n+1))
# print(f"time fot function execution is:{time}")
#default_time function
#timeit_repeat function
mysetup = "from math import sqrt"
  
# code snippet whose execution time is to be measured 
mycode = ''' 
def example(): 
    mylist = [] 
    for x in range(100): 
        mylist.append(sqrt(x)) 
'''
  
# timeit statement 
print (timeit.timeit(setup = mysetup,stmt = mycode,number = 10000)
       
