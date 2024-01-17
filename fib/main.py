# --- Directions
# Print out the n-th entry in the fibonacci series.
# The fibonacci series is an ordering of numbers where
# each number is the sum of the preceeding two.
# For example, the sequence
#  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# forms the first ten entries of the fibonacci series.
# Example:
#   fib(4) === 3

def fib(num):
    list1 = [0, 1]

    if num > 1:
        for x in range(0, num):
            nextnumber = list1[x] + list1[x+1]
            list1.append(nextnumber)
    return list1[num]