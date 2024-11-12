# Part 1
# Groups a list of integers into a list of lists of 3 integers
def groups_of_3(nums: list[int]) -> list[list[int]]:
    #nums is expected to be a list of integers and is expected to return a list of lists of 3 integers
    count = 0
    new_list = []
    final_list = []
    while True: # Repeats until broken out of
        if len(nums) > 0: # adds number to new_list, repeats 3 times
            if count < 3:
                new_list.append(nums.pop(0))
                count += 1
            else: # adds new_list to final_list and starts again
                count = 1
                final_list.append(new_list)
                new_list = [nums.pop(0)]
        else:
            final_list.append(new_list)
            break # Breaks out of while loop
    return final_list
    #returns a list of lists of 3 integers