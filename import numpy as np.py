# import numpy as np 
# arr = np.array([1,2,3,4], ndmin=2)
# print(arr)

# import numpy as np



# arr1 = [1,2,3, 4, 6, 8]
# result = arr1.rev(4)
# print(result)

# def positive_negative(number):
#     if number > 0:
#         return "positive"
#     else:
#         return "negative"
    
# res= positive_negative(4)
# print(res)

# def swap(x, y):
#     x = x + y
#     y = x - y
#     x = x - y
#     return x, y
# print(swap(1,2))

#  # write a program to find the leap year
# year = 2024
# if(year%4 ==0 and year%100 != 0)or( year%400==0 ):
#     print("leap year")
# else:
#     print("not leap year")


    # prime number program
# num = 10
# isprime = True

# if num <= 1:
#     isprime = False
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             isprime = False
#             break

# if isprime:
#     print("It is a prime number")
# else:
#     print("It is not prime number")






    

# Question: Create a 1D NumPy array with the numbers from 1 to 10.
import numpy as np
arr = np.arange(1,11)
print(arr)

# Question: Create two 1D NumPy arrays, a = [1, 2, 3] and b = [4, 5, 6]. Perform element-wise addition, subtraction, multiplication, and division.

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# Question: Create a 1D array with the values [1, 2, 3, 4, 5, 6] and reshape it into a 2x3 2D array.
arr = np.array([1, 2, 3, 4, 5, 6])
arr = arr.reshape(2,3)
print(arr)
arr = np.array([1, 2, 3, 4, 5, 6,7,8])
arr = arr.reshape(4,2)
print(arr)


# Question: Create a 2D array arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]. Access the element at the second row and third column.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[1][2])
 
# Inersection of two array
arr1= np.array([1,2,3,4],[3,4,5,6]) 
arr2= np.array([3,4,5,6],[7,8,9,5])
intersection= np.intersect1d(arr1, arr2)	
print("Intersection of two array:",intersection)

# Write a function to  check given array is present in an ascending order or not 
def check_order(arr):
        if len(arr) <= 1:
           return True
        for i in range(len(arr) - 1):
           if arr[i] > arr[i + 1]:
            return False
        return True
print(check_order([20, 1, 7, 10]))

      
      


      


