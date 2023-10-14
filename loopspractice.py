x=1
while x<=10:
    print(x)
    x+=1
print()

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print()
sum=0
for i in range(1,11):
    sum+=i
print(sum)
print()

for i in range(1,11):
    print(i*2)
print()

numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num>500:
        break
    elif num>150:
        continue
    elif num%5==0:
        print(num)
print()

x=6666666
count=0
while x!=0:
    x=x//10
    count+=1
print(count)

n=5
for i in range(0,n+1):
    for j in range(n-i,0,-1):
        print(j,end=" ")
    print()

print()

list1 = [10, 20, 30, 40, 50]
list2= reversed(list1)
for i in list2:
    print(i)
print()

for i in range(-11,0,1):
    print(i)

print()

for i in range(5):
    print(i)
else:
    print("done!")
print()
print('printing prime numbers')

for num in range(25,50):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
print()
print('Fibonacci sequence:')
num1=0
num2=1
for i in range(10):
    print(num1,end=' ')
    res=num1+num2

    num1=num2
    num2=res
print()
n=5
factorial=1
for i in range(n,1,-1):
    factorial*=i
print(factorial)
print()
print("reversing the integer")
num=234567
reverse_num=0
while num>0:
    rem=num%10
    reverse_num=(reverse_num*10)+rem
    num=num//10
print(reverse_num)
print()

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in my_list[1::2]:
    print(i,end=' ')
print()

for i in range(1,7):
    print(i**3)
print()










