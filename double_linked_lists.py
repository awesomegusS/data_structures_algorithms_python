class Node():
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList():
    def __init__(self):
        '''empty list'''
        self.head = None

    def if_no_elem(self):
        '''handles no element'''
        if self.head is None:
            print('Linked List is empty')
            return

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count+=1
        return count


    def print_forward(self):
        self.if_no_elem() #handle no element

        #iterate through list objects
        itr = self.head
        dll_str = ''
        while itr:
            dll_str += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(dll_str)


    def print_backward(self):
        self.if_no_elem() #handle no element

        #iterate through list objects
        itr = self.head 
        dll_str = ''
        while itr:
            if itr.next is None: #found last elem
                while itr:
                    dll_str+= str(itr.data) + ' --> ' if itr.prev else str(itr.data)
                    itr = itr.prev
                break
            itr = itr.next
        
      
        print(dll_str)


    def insert_at_beginning(self, data):
        #handle empty list
        if self.head is None:
            self.head = Node(data)
            return  
        
        #non-empty list
        node = Node(data, next=self.head) #insert data in front of list
        self.head.prev = node #update previous pointer
        self.head = node
        
    
    def insert_at_end(self, data):
        #empty list
        if self.head is None:
            node = Node(data)
            self.head = node
            return
        
        #non-empty list
        #iterate through list objects until last elem
        itr = self.head
        while itr.next:  
            itr = itr.next
        itr.next = Node(data, next=None, prev=itr)

    def insert_values(self, data_list):
        #insert values given a list
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr) #new elem in dll
                if node.next:
                    itr.next.prev = node #update next elem previous pointer to new elem
                itr.next = node #insert data by updating current elem next pointer
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                if itr.next:
                    itr.next.prev = itr
                break

            itr = itr.next
            count+=1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            raise Exception('Empty linked list')

        #handle first elem
        if self.head.data == data_after:
            node = Node(data_to_insert, self.head.next, prev=self.head) #new elem in dll
            self.head.next.prev = node #update next elem previous pointer to new elem
            self.head.next = node #insert data by updating current elem next pointer
            return

        #iterate through list objects
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next, itr)
                if node.next:
                    itr.next.prev = node
                itr.next = node
                break

            itr = itr.next
            #handle unfound value
            if itr.next is None:
                raise Exception('data_after not found')

    def remove_by_value(self, data):
        #handle empty linked list
        if self.head is None:
            return

        # handle first elem
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            return

        #iterate through list objects
        itr = self.head
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                if itr.next:
                    itr.next.prev = itr
                break
            itr = itr.next
            #handle unfound value
            if itr.next is None:
                raise Exception('data not found')


#testing
if __name__ == '__main__':
    dll = DoubleLinkedList()
    dll.insert_at_beginning(1)
    dll.insert_at_beginning(2)
    dll.insert_at_beginning(3)
    print('Double Linked List')
    dll.print_forward()
    dll.print_backward()
    print('-'*40)

    #-------insert values test-------
    # print('testing insert values')
    # dll.print_backward() #reversed
    # dll.insert_values(["banana","mango","grapes","orange"])
    # dll.print_forward()
    # dll.print_backward() #reversed
    #print('-'*40)

    #------modifiers at index test-----
    print('testing modifiers by index')
    dll.insert_at(0, 4) #beginning
    dll.print_forward()
    dll.insert_at(4, 0.5) #end
    dll.print_forward()
    dll.remove_at(0) #beginning
    dll.print_forward()
    dll.remove_at(3) #end
    dll.print_forward()
    dll.remove_at(1) #middle
    dll.print_forward()
    dll.print_backward()
    print('-'*40)

    #-----modifiers by value test------
    #adds and removes the value 1.5
    # print('testing modifiers by value')
    # dll.insert_after_value(2, 1.5)
    # dll.print_forward()
    # dll.print_backward()
    # dll.remove_by_value(1.5)
    # dll.print_forward()
    # dll.print_backward()
    # print('\n')
    # dll.insert_after_value(3, 2.5)
    # dll.print_forward()
    # dll.print_backward()
    # print('\n')
    # dll.remove_by_value(3)
    # dll.print_forward()
    # dll.print_backward()
    # print('-'*40)


