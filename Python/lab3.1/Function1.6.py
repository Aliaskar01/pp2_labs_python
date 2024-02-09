def reverse(string):
    string_list = string.split()
    for i in range(len(string_list)-1, -1, -1):
        print(string_list[i], end = ' ')

string_input = input()
reverse(string_input)