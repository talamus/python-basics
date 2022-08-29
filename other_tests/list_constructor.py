original_list_or_tuple_or_anything_listlike = ["apple", "banana", "cherry"]

this_list = list(original_list_or_tuple_or_anything_listlike) # make a new list! 
#this_list = original_list_or_tuple_or_anything_listlike   # <-- this would force both lists to be same 
this_list.pop() # remove cherry!

print("this_list:", this_list)
print("original_list:", original_list_or_tuple_or_anything_listlike)
