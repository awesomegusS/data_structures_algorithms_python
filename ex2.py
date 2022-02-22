stonks = {}
path = '/Users/ikwang/Downloads/Code/DSA/data-structures-algorithms-python-master/data_structures/4_HashTable_2_Collisions/Solution/nyc_weather.csv'
with open(path, 'r') as f:
    count = 0
    for line in f:
        if count == 0:
            count+=1
            continue
        token = line.split(',')
        day = str(token[0])
        price = float(token[1])
        stonks[day] = price

print(sum(stonks.values())/len(stonks))

path = '/Users/ikwang/Downloads/Code/DSA/data-structures-algorithms-python-master/data_structures/4_HashTable_2_Collisions/Solution/poem.txt'
poem = {}

with open(path, 'r') as f:
    for line in f:
        words = line.split()
        for word in words:
            poem.setdefault(word, 0)
            poem[word] += 1

print(poem)


