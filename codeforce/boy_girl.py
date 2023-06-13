name = input()
chk = ""
for i in name:
    if i not in chk:
        chk += i
if len(chk) %2 != 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")