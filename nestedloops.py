for i in range(3):
    print(i)
    for j in range(7,9):
        print(j)

print()

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(str(j)+""*n,end=" ")
    print()

print()

n=4
for i in range(1,n+1):
    for j in range(i):
        print(str(i)+' ',end='')
    print()

print()

sam='python is highperformance  language'
for i in sam:
    if i=='a'or  i=='e'or i=='i' or i=='o'or i=='u' :
        continue
    print(i,end='')
print()

n=5
for i in range(1,n+1):
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(1,n+1):
    for j in range(n-i):
        print("*",end=" ")
    print()

print()
print("Triangle")
print()
n=5
for i in range(1,n+1):
    print(" "*(n-i)+i*" *" )

print()
print("Invertd Triangle")
n=5

for i in range(1,n+1):
    print(" "*i + " *"*(n-i))

print()

n=65
for i in range(1,6):
    for j in range(1,i+1):
        ch=chr(n)
        print(ch,end=' ')
        n+=1
    print()

print()

n=65
for i in range(1,6):
    for j in range(i):
        print(chr(n),end=" ")
    print()
print()

n=65
for i in range(1,6):
    for j in range(i):
        print(chr(n+(i-1)),end=" ")
    print()

print()

n=65
k=4
for i in range(1,k+1):
    for j in range(i):
        print(chr(n+(j)),end=" ")
    print()
print()

print("printed my name in rows and coloumns")

name='srikanth'
for i in range(5):
    for j in range(3):
        print(name,end="  ")
    print()
print()