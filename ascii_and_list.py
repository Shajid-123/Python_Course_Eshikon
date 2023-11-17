list_1 = [["ab"],["cd"],["ef"]]
list_2 = []
sum = 0


for row in list_1:
    for col in row:
        for char in col:
         ascii = (ord(char))
         list_2.append(ascii)


            




print(list_2)

# for row in range(len(list)): #row = 0;1;
#     col_size = len(list[row]) # col size =3
#     for col in range(col_size): 
#         print(list[row][col])