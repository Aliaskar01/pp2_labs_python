def unique(list):
    new_list = []
    for i in range(len(list)):
        find = False
        for j in range(i):
            if list[i] == list[j]:
                find = True
                try:
                    new_list.remove(list[i])
                except:
                    pass
        if not find:
            new_list.append(list[i])
    return new_list

num_input = input()
num_list = num_input.split()
print(*unique(num_list))