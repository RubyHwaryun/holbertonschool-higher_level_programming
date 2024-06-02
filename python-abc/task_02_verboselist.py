#!usr/bin/python3

class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        super().extend(iterable)
        num_items = len(iterable)
        print(f"Extended the list with {num_items} items.")

    def remove(self, item):
        if item in self:
            print(f"Removed {item} from the list.")
        else:
            print(f"{item} not found in the list.")
        super().remove(item)

    def pop(self, index=-1):
        if index == -1:
            popped_item = self[-1]
            print(f"Popped {popped_item} from the list.")
        else:
            popped_item = self[index]
            print(f"Popped {popped_item} from the list.")
        return super().pop(index)

# Testing the VerboseList class
verbose_list = VerboseList([1, 2, 3])

verbose_list.append(4)
verbose_list.extend([5, 6, 7])
verbose_list.remove(3)
verbose_list.pop()

