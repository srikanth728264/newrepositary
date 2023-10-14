input='My name is Vignesh'
store=[]
str=''
for i in range(len(input)) :
    if input[i]==' ':
        store.append(i)
for j in input:
    str=j+str
rev=''.join(str.split(' '))
for k in store :
    rev = rev[:k] + ' ' + rev[k:]
print(rev)

list=[9,1,3,4,0,5]
target=5
n=len(list)
for i in range(n) :
    for j in range(i,n):
        if list[i]+list[j] == target :
            print(i,j)