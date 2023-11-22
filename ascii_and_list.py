list1 = ["ab","cd","ef"]
list2 = []
for i in list1:
    for j in i:
        sum = 0
        ascii = ord(j)
        asc = sum+ascii
        list2.append(asc)
print(list2)
