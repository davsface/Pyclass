import copy
#
num_list_1 = [2,9,7]
num_list_2 = [2,9,7]
print(num_list_1 == num_list_2) # Test whether num_list_1 and num_list_2 are equal
print(num_list_1 is num_list_2) # Test whether they refer to the same object
num_list_1 = num_list_2 # Now they refer to the same object
print(num_list_1 is num_list_2)
num_list_2 = [23,-1,19] # Make num_list_2 refer to a different object
print(num_list_1 is num_list_2)
#
# num_list_1 = [3,17,12]
# num_list_2 = num_list_1 # num_list_1 and num_list_2 refer to the same object
# print(num_list_1 is num_list_2)
# num_list_2[0] = 99 # Change the object that num_list_1 and num_list_2 both refer to
# print(num_list_1)
# print(num_list_1 is num_list_2)

# first example
# def square_val(val):
#   val = val * val
#   print(val)
#
# num = 8
# square_val(num)
# print(num)
# #
# # # second example
# def square_val(val):
#     val[0] = val[0] * val[0]
#     print(val)
#
#
# num_list = [8]
# square_val(num_list)
# print(num_list)
#
#
# #second example
# def square_val(val):
#     deep_copy_num = copy.deepcopy(val)
#     deep_copy_num[0] = deep_copy_num[0] * deep_copy_num[0]
#     print(deep_copy_num)
#
#
# num_list = [8]
# square_val(num_list)
# print(num_list)