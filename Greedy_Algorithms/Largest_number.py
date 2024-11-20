""" What is the largest number that consists of digits 3, 9, 5, 9, 7, 1? Use all the digits."""

#get input and split numbers
lst_of_numbers = list(map(int, input("Enter Numbers with Space ==>").split()))
result = "" 

#without sorting
while(lst_of_numbers):
    max_in_lst = lst_of_numbers[0]
    index_max = 0
    for i in range(len(lst_of_numbers)):
        if lst_of_numbers[i] > max_in_lst:
            max_in_lst = lst_of_numbers[i]
            index_max = i
    lst_of_numbers.pop(index_max)
    result += str(max_in_lst)
print(int(result))
