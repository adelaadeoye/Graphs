# create a function
# create a sum variable
# loop through the array
    # sma

#     if found add to sum



def sum(array):
    sum=0
    for element in array:
       sum += min(element)
    return sum

print(sum([[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]))