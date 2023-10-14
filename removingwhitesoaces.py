input_string="enter the string:::"
output_string=input_string.replace(' ','')
print(output_string)

print()
input_string="enter the string:::"
output_string=''.join([char for char in input_string if char!=" "])
print(output_string)
print()
input_string="enter the string:::"
out=''
for i in input_string:
    if i ==' ':
        del i
    else:
        out+=i
print(out)
print()

s="To remove spaces from a string using a for loop without creating a new variable, you can convert the string to a list of characters, iterate through the list to remove spaces, and then join the characters back into a string. Here's an example:"
x=s.split(' ')
y={}
for i in x :
    if i in y :
        y[i]+=1
    else:
        y[i]=1
print(max(y))
key,value = max((k,v) for k,v in y.items())

print(key)
print(value)
