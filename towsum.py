my_list = [4,7,3,5,2,1]
target = 8
newdict = dict()
for i in range(len(my_list)):
    p = target - my_list[i]
    if p not in newdict:
        newdict[my_list[i]] = i
    else:
        print(newdict[p],i)