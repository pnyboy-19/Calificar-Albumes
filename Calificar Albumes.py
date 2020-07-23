lst=[]
suma = 0
print("data: ")
A=int(input())
for x in range(A):
  B=float(input())  
  lst.append(B)
for i in range(0,len(lst)):
    suma = suma+lst[i]
C=suma/A
print(f"answer: {C}")

    
