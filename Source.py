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
'''


#Single Number
#works if starting with 1 (need negatives as well)
#nums = [4,1,2,1,2]
#missing = []

'''
for i in range(len(nums)):
    if i+1 in nums:
        missing.append(True)
    else:
        missing.append(False)

for i in range(len(missing)):
    if missing[i] == True:
        result = nums.count(i+1)
        if(result != 2):
            print(i+1) #return i+1
            '''


#Single Number (works for negatives)
'''
nums = [1,1,0,-1,0,-2,-2]
missing = []
counter = 0
for i in range(min(nums), max(nums)+1):

    if min(nums) + counter in nums:
        missing.append(True)
    else:
        missing.append(False)
    counter += 1

for i in range(len(missing)):
    if missing[i] == True:
        result = nums.count(min(nums) + i)
        if (result != 2):
            print(min(nums) + i) #return min(nums) + i
'''

#Single Number
# set of letters
nums = [0,1,1,-1,-1]


container = set([])


for i in range(len(nums)):

    if nums[i] in container:
        container.remove(nums[i])
    else:
        container.add(nums[i])

print(list(container)[0]) #return list(container)[0]