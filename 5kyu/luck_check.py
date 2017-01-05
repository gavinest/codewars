'''
Description:

In some countries of former Soviet Union there was a belief about lucky tickets. A transport ticket of any sort was believed to posess luck if sum of digits on the left half of its number was equal to the sum of digits on the right half. Here are examples of such numbers:

003111    #             3 = 1 + 1 + 1
813372    #     8 + 1 + 3 = 3 + 7 + 2
17935     #         1 + 7 = 3 + 5
56328116  # 5 + 6 + 3 + 2 = 8 + 1 + 1 + 6
Such tickets were either eaten after being used or collected for bragging rights.

Your task is to write a funtion luck_check(str), which returns true/True if argument is string decimal representation of a lucky ticket number, or false/False for all other numbers. It should throw errors for empty strings or strings which don't represent a decimal number.
'''

def luck_check(string):
    try:
         int(string)
    except ValueError as e:
        raise e
    else:
        n = int(len(string) / 2)
        half_1 = sum(map(int, string[:n]))
        half_2 = sum(map(int, string[-n:]))
        if half_1 == half_2:
            return True
        else:
            return False

if __name__ == '__main__':
    print luck_check('5555')
