#1
import numpy as np
arr=np.array([
    [37.5,36.7,45.0],
    [36.5,32.7,32.0],
    [37.1,31.7,40.0],
    [27.4,36.7,45.0],
    [37.5,26.7,35.0],
    [37.5,31.7,25.0]
    ])
l1=[]
for x in range(0,6):
    l1.append(np.mean(x))
print(l1)
print("Max",max(l1))
print("Min",min(l1))


#2
import numpy as np
arr=np.array([
    [5.54,3.38,7.99],
    [3.54,4.38,6.99],
    [1.54,2.39,9.29]
     
    ])
print("Original Array\n")
print(arr)
print("\nNumber between 5 to 8\n")
for x in arr:
    for y in x:
        if( y>=5 and y<=8):
            print(y)
        
    
#3  
import numpy as np
arr=np.array([
        [5,3,7],
        [3,4,6],
        [1,2,9]
         ])
arr[arr == 3] = 20
print(arr)

#4
import numpy as np
arr=np.array([
        [5,3,7],
        [3,4,6],
        [1,2,9]
         ])
print(np.flip(arr))   #reverse every element
print(np.flipud(arr))   #reverse row wise

#5
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
for x in range (0,len(a)):
    a[x]=np.flip(a[x])
print(a)


#6 Printing Unique number in sorted order
import numpy as np
a=np.array([1,2,7,4.5,96,40,98,701,90,101])
print(a)
b=np.array([1,2,3,45,96,40,98,701,2,3,7])
print(b)
print(np.union1d(a,b))
            
     
 