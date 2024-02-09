def spy_gam(nums):
    has01 = False
    has02 = False
    has7 = False
    for i in range(1, len(nums)):
        if nums[i] == '0' and not has01:
            has01 = True
        elif nums[i] == '0' and not has02:
            has02 = True
        elif nums[i] == '7' and not has7:
            has7 = True
    return has7

num_input = input()
num_list = num_input.split(",")

print(spy_gam(num_list))