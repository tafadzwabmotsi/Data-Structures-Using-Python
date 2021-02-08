from data_structures.linked_list import LinkedList

l_list: LinkedList = LinkedList()

l_list.append(10)
l_list.append(20)
l_list.append(23)
l_list.append(45)
l_list.append(67)


if __name__ == '__main__':
    l_list.print_elements()
    l_list.reverse()
    l_list.print_elements()



