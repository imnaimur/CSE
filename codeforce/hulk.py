n = int(input())
s = ""
for i in range(n):
    if i%2 == 0:
        s+= "I hate"
        if i +1 == n:
            s+= " it"
        else:
            s+= " that "
    else:
        s += "I love"
        if i +1 == n:
            s+= " it"
        else:
            s+= " that "
print(s)