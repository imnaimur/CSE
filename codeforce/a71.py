n = int(input())
list1 = []
list2 = []
for i in range(n):
    itm = input()
    list1.append(itm)
for i in list1:
    if len(i)>10:
        x = i[0] + str(len(i)-2) +i[len(i)-1]
        list2.append(x)
    else:
        list2.append(i)
print("\n".join(list2))