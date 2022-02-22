class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None

    def print(self):
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)
        
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

    def insert_at_beginning(self, data):
        self.head = Node(data, self.head)
    
    def insert_at_end(self, data):
        # if empty linked list
        if self.head is None:   
            node = Node(data, None)
            self.head = node
            return

        # if list not empty
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)


    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

# EXCERCISE

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            raise Exception('Empty linked list')

        #handle first elem
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
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
            return

        itr = self.head
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
            #handle unfound value
            if itr.next is None:
                raise Exception('data not found')
            
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value('mango', 'apple')
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    # ll.remove_by_value("figs")
    # ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.print()



