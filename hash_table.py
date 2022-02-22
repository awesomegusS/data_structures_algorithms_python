class HashTable:  
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]
            
    def __setitem__(self, key, val):
        #separate chaining to solve collision
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
        if not found:
            self.arr[h].append((key,val))
        
    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del",index)
                del self.arr[arr_index][index]


#my implementation
class LHashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX  

    def __getitem__(self, key):
        h = self.get_hash(key)
        #if no value
        if self.arr[h] is None:
            return 
        
        #if hash collision occurs
        if self.arr[h][0] != key:
            for elem in self.arr:
                if elem:
                    if elem[0] == key:
                        return elem[1]
        else:
            return self.arr[h][1]

    def __setitem__(self, key, val):
        #check if hash table is full
        item_count = 0
        for data in self.arr:
            if data != None:
                item_count += len(data)
        if item_count == self.MAX * 2:
            raise Exception('Hashtable Full')

        
        #Linear probing to solve collision
        h = self.get_hash(key)
        found = False
        if self.arr[h] is None:
            self.arr[h] = (key, val)

        elif self.arr[h][0] == key: #modify value if key exists
            self.arr[h] = (key, val)

        elif not found:
            #check after
            for arr_idx, elem in enumerate(self.arr[h:]):
                if elem is None:
                    self.arr[h+arr_idx] = (key, val)
                    found = True
                    break

            #check before
            if not found:
                for arr_idx, elem in enumerate(self.arr[0:h]):
                    if elem is None:
                        self.arr[arr_idx] = (key, val)
                        found = True
                        break     
        
            

if __name__ == '__main__':    
    t = LHashTable()
    t['Jan'] = 1
    t['Feb'] = 2
    t['Mar'] = 3
    t['Apr'] = 4
    t['May'] = 5
    t['Jun'] = 6
    t['Jul'] = 7
    t['Aug'] = 8
    t['Sept'] = 9
    # t['Oct'] = 10
    # print(t.arr)
    # t['Nov'] = 11 # raises excetption
    # t['Dec'] = 13
    # print(len(t.arr))

    print(t['Jan'])
    print(t['Feb'])
    print(t['Mar'])
    print(t['Apr'])
    print(t['May'])
    print(t['Jun'])
    print(t['Jul'])
    print(t['Aug'])
    print(t['Sept'])
    print(t['Dec'])
    print(t.arr)

