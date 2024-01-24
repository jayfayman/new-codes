num = int(input())
integer_list = map(int, input().split())
integer_list = list(integer_list)
integer_list = integer_list[:num]
my_tuple = tuple(integer_list)
print (my_tuple)
result = hash(my_tuple)
print(result)
