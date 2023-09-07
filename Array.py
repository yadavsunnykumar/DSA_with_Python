# Python append() Method

import array as arr

array1 = arr.array('i', [1, 2, 3, 4, 5, 6])
print("The values of the array are: ", end=" ")
for i in range(0, len(array1)):
    print(array1[i], end=" ")
print('\r')

# append() method
array1.append(7)

print("The new array after appending values are ", end=" ")
for j in range(0, len(array1)):
    print(array1[j], end=" ")

print('\r')
# insert() function

array1.insert(2, 10)
print("After inserting an element in the array ", end=" ")
for k in range(0, len(array1)):
    print(array1[k], end=" ")

print('\r')
# pop() function

array1.pop()# we also can specify the index to pop the elements.
print("The elements of the array after pop() function ", end=" ")
for l in range(0, len(array1)):
    print(array1[l], end=" ")

print('\r')
array1.append(1)

array1.remove(1)
print("Array elements after removing the first occurence ", end =" ")
for m in range (0,len(array1)):
    print(array1[m] ,end=' ')


print("\r")
array1.reverse()

print("The reversed array  are ",end=" ")
for n in range(0,len(array1)):
    print(array1[n],end=" ")

print("\r")

print(f'The element 2 is located at {array1.index(2)}')