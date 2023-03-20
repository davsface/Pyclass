# Given two lists, key = [1,2,3,4,5,6,7,8,9,10,11,12] and value = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
# combine these into a single dictionary

key = [1,2,3,4,5,6,7,8,9,10,11,12]
value = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


months = {key[i]: value[i] for i in range(12)}

# for i in range(12):
#     months[key[i]] = value[i]
print(months)