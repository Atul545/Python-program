import numpy as np
a1=np.array([1000,5000,1000,6000,7000])
k=6000
for x in a1:
    
    for y in a1:
        if x+y==k :
            print (x,y)




import numpy as np

a2 = np.array([0, 10, 55, 64, 97, 100, 70])
a3 = np.array([0, 70])
result = np.isin(a2, a3)

 
print(result)







