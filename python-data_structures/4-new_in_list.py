def new_in_list(my_list, idx, element):
  new_in_list = my_list[:]
  if idx < 0:
    return new_in_list
  if idx >= 0:
    return new_in_list
  else:
    new_in_list[idx] = element
    return new_in_list
