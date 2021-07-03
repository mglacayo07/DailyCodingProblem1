# Daily Coding Problem: Problem #1[Easy]

# Good morning! Here's your coding interview problem for today.
#
# This problem was recently asked by Google.
#
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

def addupto(list, k):
    for x in range(0, len(list)):
        for y in range(x+1, len(list)):
            if (list[x]+list[y]) == k:
                print(str(list[x]) + " + " + str(list[y]) + " = " + str(k))
                return True
    return False

if __name__ == '__main__':

    list_of_numbers = [10, 15, 3, 7]
    k = 10

    print("My list: ", list_of_numbers)
    print("k value: ", k)
    print(addupto(list_of_numbers,k))



