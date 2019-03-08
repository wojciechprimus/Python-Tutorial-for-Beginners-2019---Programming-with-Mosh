list=[13,7,7,7,18,13,82,333,18,15,16,90,82,7]
uniques_value=[]

for i in list:
    if i not in uniques_value:
        uniques_value.append(i)

print(uniques_value)

