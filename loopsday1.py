string="nikhil"
output=""

for i in range(len(string)):
    output=string[i]+output

print(output)

string="python is most powerful language"
output={}

for i in string:
    if i in output:
        output[i]+=1

    elif i==' ':
        del i

    else:
        output[i]=1


print(output)








