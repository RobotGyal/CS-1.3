"""
PROBLEM

Remove duplicates from array (list)

"""

### RESTATE ###
# Remove duplicates from array (list)

### QUESTIONS ###
# 
#
#
#

## ASSUMPTIONS ###
# whole numbers
# sorted
# return a list
#
#

### PSUEDOCODE ###
# iterate through list
# if same number found...dont' add to new list...continue to next 'node'
# if not found...add to new list
# return list


# setup test variables
nums = [3,4,4,4,4,5,5]

# write function
def remove_duplicates(nums):
    """
    # description

    Vars:
    """
    no_duplicates   = []
    for i in nums:
        if nums[i] not in no_duplicates:
            print('whattt')
            no_duplicates.append(nums[i])
        else:
            print('i')
    return no_duplicates



# Testing...
print(remove_duplicates(nums))