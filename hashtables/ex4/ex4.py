def has_negatives(array):

    result = []
    number_list = {}
    
    #loop through the array and hash
    for number in array:
        # if there is an absolute value
        if number_list.get(abs(number)) is not None:
            #add to the number_list
            number_list[abs(number)] += 1
        else:
            #otherwise if no absolute value, give value of 1
            number_list[abs(number)] = 1
    #filter through number_list
    for number in number_list:
        #if value greater than one 
        if number_list[number] > 1:
            #add to the result
            result.append(number)

    return result



if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
