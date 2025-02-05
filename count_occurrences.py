def count_occurrences(numbers, target):
    counter=0
    for i in numbers:
        if i==target:
            counter+=1
    return counter