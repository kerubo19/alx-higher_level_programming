#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for element in my_list:
        # check if the element is equal to the search value
        if element == search:
            # replace the element with the replace value and append it to the new list
            new_list.append(replace)
        else:
            # keep the element as it is and append it to the new list
            new_list.append(element)
    # return the new list
    return new_list
