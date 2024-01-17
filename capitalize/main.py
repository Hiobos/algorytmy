# --- Directions
# Write a function that accepts a string.  The function should
# capitalize the first letter of each word in the string then
# return the capitalized string.
# --- Examples
#   capitalize('a short sentence') --> 'A Short Sentence'
#   capitalize('a lazy fox') --> 'A Lazy Fox'
#   capitalize('look, it is working!') --> 'Look, It Is Working!'

def capitalize(str):
    list1 = str.split()
    for x in range(0, len(list1)):
        list1[x] = list1[x].capitalize()
    list1 = (" ").join(list1)
    return list1