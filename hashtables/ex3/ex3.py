def intersection(arrays):
    """
    YOUR CODE HERE
    """
    result = []
    number_table = {}
    #first array will be hash through
    for number in arrays[0]:
        # set first array as first entry in number_table
        number_table[number] = 1
    #cross reference next array with previous array to check for duplicates
    for i in range(1,len(arrays)):
        #check through each number in array
        for number in arrays[i]:
            #if number inside of number_table isnt none
            if number_table.get(number) is not None:
                # add 1
                number_table[number] += 1
    #final check inside the number_table
    for number in number_table:
        #if greater than one instance
        if number_table[number] > 1:
            #append to the result list
            result.append(number)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
