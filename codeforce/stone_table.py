n = int(input())
stone = input()
ls2 = ""
for i in range(n-1):
    if stone[i] == stone[i+1]:
        ls2+= stone[i]
print(len(ls2))