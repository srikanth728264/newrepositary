'''x= " '04','nx':'02','xx' "
y= x.replace(':',',').replace("'",'').split(",")
li=[item.replace("'",'') for item in y]
print(li[:2])'''

'''num=1234567
rev=0
while num>0 :
    rev=num%10 + rev*10
    num=num//10
print(rev)'''

'''st='helloworld'
es=''
for i in st :
    es=i+es
print(es)'''

'''str='python is a good programming language'
res={}
for i in str:
    if i==' ':
        del i
    elif i in res:
        res[i]+=1
    else:
        res[i]=1
print(res)'''

test='''git branch: Lists all branches in the repository.
git branch <branch_name>: Creates a new branch.
git checkout <branch_name>: Switches to a different branch.
git merge <branch_name>: Merges changes from one branch into the current branch.
Pull and Push Changes:

git pull origin <branch_name>: Pulls changes from a remote repository into your local branch.
git push origin <branch_name>: Pushes your local branch changes to the remote repository.'''

test1=test.split(" ")
count={}
for i in test1:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
max_value=max(count.values())
print(count[max_value])