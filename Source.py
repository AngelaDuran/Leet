# Duplicate check (COMPLETE), used 20.1 MB of memory
'''
l1 = [1, 2, 3, 4]
l2 = [1, 2, 3, 3]


def checkDouble(l):
    if len(l) == len(set(l)):
        print("Does not")
        return False
    else:
        print("Has")
        return True

print(checkDouble(l1))
'''

# Missing Numbers (Complete), used 	15.5 MB of memory

nums = [3, 0, 1]
# nums = [1]

def checkMissing(nums):
    n = len(nums)

    for x in range(len(nums) + 1):
        if (n in nums):
            n = n - 1
        else:
            # print("OUTPUT: " + str(n))
            return n
        # n = n - 1  #maybe need if not accepted


print("Output: " + str(checkMissing(nums)))


