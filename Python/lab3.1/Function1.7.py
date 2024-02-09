def has_33(nums):
    has = False
    for i in range(1, len(nums)):
        if (nums[i] == '3' or nums[i] == '3,') and nums[i-1] == '3,':
            has = True
    return has

num_input = input()
num_list = num_input.split()

print(has_33(num_list))