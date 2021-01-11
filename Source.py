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
