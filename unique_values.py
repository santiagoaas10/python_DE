def find_unique_elements(lst):
    return len(set(lst))

#o tambn
def find_unique_elements(lst):
    new_lst=[]
    for num in lst:
        if num not in new_lst:
            new_lst.append(num)
        # your code here
    return len(new_lst)