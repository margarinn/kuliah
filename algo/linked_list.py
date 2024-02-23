class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.iteration = 0 

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        # Adding new node to the end of the list
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head

        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node


    def print_list(self):
        # view all node
        cur_node = self.head

        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
        
    def delete_node(self, key):
        # self explanotory
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        
        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def search(self, key):
        cur_node = self.head
        num = cur_node.iteration

        while cur_node:
            num += 1
            if cur_node.data == key:
                print(num)
                return True

            cur_node = cur_node.next

        return False

    def adv_insert(self, key):
        pass
    
    def adv_delete(self, key):
        pass

def main():
    list = LinkedList()

    #add
    list.append("A")
    list.append("B")
    list.append("C")

    print(list.search("C"))
    
    # show list
    print("LinkedList: ")
    list.print_list()

    print("#" * 20)
    # delete
    list.delete_node("B")
    list.print_list()


    print("# " * 20)
    # search

    print(list.search("C"))
    print(list.search("X"))



if __name__ == "__main__":
    main()