def intersection(arrays):
  
    # Your code here
    d = {}

    for index, l in enumerate(arrays):
        for num in l:
            if num not in d:
                # set a key for that number with it's value as an array containing the index of list it appeared in 
                d[num] = [index]
            else:
                # add the current list index to the entry for this num 
                d[num].append(index)
    

    # if len(arrays) = len(the value of that key), we have an intersection point, put that key in the result 

    # may have to convert array values to tuples to eliminate dups 

    result = []

    for key in d:
        # might need to change to tuple here 
    
        if len(d[key]) == len(arrays):
            result.append(key)


    return result

array1 = [
    [1, 2, 3, 4, 5],
    [12, 7, 2, 9, 1],
    [99, 2, 7, 1,]
]

print(intersection(array1))



# if __name__ == "__main__":
#     arrays = []

#     arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
#     arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
#     arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

#     print(intersection(arrays))
