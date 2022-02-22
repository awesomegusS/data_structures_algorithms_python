
expenses = [2200, 2350, 2600, 2130, 2190]
print(expenses)

expenses_json = [
    {'Jan': 2200},
    {'Feb': 2350},
    {'Mar': 2600},
    {'Apr': 2130},
    {'May': 2190}
]

#1 How many dollars was spent in Feb compared to Jan

diff_Jan_Feb = expenses[1] - expenses[0]

#2 Total expense in Q1

Q1_expenditure = sum(expenses[0:3])
print(Q1_expenditure)

#3 spent 2k?

if 2000 in expenses:
    print('2000 dollars was spent in {}'.format(expenses.index(2000)))
else:
    print('None found')

#4 
expenses.append(1980)

#5
expenses[3] -= 200
print(expenses)

print('\n',dir(list))

#6 
heroes = ['spider man','thor','hulk','iron man','captain america']

heroes[1:3] = ['Doctor Strange']
print(heroes)
