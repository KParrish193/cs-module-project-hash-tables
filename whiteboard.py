# Print out all of the numbers in the following array that are divisible by 3:
# /3
# The expected output for the above input is:
# 27
# 81
# 9
# 27
# 99
# 63
# 42
# You may use whatever programming language you wish.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.


array = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

for i in array:
    if i%3 == 0:  
        print(i)


# Print out all of the strings in the following array that represent a number divisible by 3:
# [
#   "five",
#   "twenty six",
#   "nine hundred ninety nine,
#   "twelve",
#   "eighteen",
#   "one hundred one",
#   "fifty two",
#   "forty one",
#   "seventy seven",
#   "six",
#   "twelve",
#   "four",
#   "sixteen"
# ]
# The expected output for the above input is:
# nine hundred ninety nine
# twelve
# eighteen
# six
# twelve
# You may use whatever programming language you wish.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.




# Add up and print the sum of the all of the minimum elements of each inner array:
# [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# The expected output is given by:
# 4 + -1 + 9 + -56 + 201 + 18 = 175
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

given = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

def mini_sum_array(given):
    # ? miniSum = 0
    sumList = []

    for i in given:
        # find the minimum for each element in given
        # ? miniSum += min(i)
        sumList.append(min(i))

        # add together results from minimums

    # return the sum
    return sum(sumList)

print(mini_sum_array(given))