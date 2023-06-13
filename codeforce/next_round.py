x = input()
x = x.split()
n,k = int(x[0]),int(x[1])
ls = []
count = 0
string = input()
string = string.split()
for i in string:
    if int(i)>=int(string[k-1]):
        if int(i) != 0:
            count+=1
print(count)