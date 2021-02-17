##Generating a 3x3 matrix with 9 random prime numbers.(You have to do it using the for loop)

#YUSUF NAS - HOMEWORK1
import random

matrix3D = [[0,0,0],[0,0,0],[0,0,0]]
primeList = []
count = 0

for prime in range(1,100):
    for mod in range(1,prime+1):
        if(prime % mod == 0):
            count+=1
    if(count==2):
        primeList.append(prime)
    count=0
    
            
print(primeList)

for i in range(len(matrix3D)):
    for j in range(len(matrix3D)):
        matrix3D[i][j] = primeList.pop(random.randint(0,len(primeList)-1))
    
    print(matrix3D[i])
    
