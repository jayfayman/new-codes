array_length, set_length = input("Enter the number of elements in the array and sets: ").split()
array_length = int(array_length)
set_length = int(set_length)
array = input("Enter the elements in the array: ").split()[:array_length]
#print(array)
set_A = input("Enter the elements in the set A: ").split()[:set_length]
set_B = input("Enter the elements in the set B: ").split()[:set_length]
set_A = set(set_A)
set_B = set(set_B)
happiness = 0
for i in range (array_length):
        if array[i] in set_A:
           happiness +=1
        elif array[i] in set_B:
            happiness -=1
        else:
            continue
print (happiness) 