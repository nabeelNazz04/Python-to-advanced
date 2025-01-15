a=set()
a.add(2)
a.add(2)
a.add(1)#or we can use a={2,2,1}
print(a)
numbers=[1,2,3,3,4,5,5]
unique_nos=set(numbers)
print(unique_nos)
unique_nos.add(7)

#frozen set is a set but it does not allow to add a new element into that set

fs=frozenset(numbers)
print(fs)
#ie,fs.add(4)will throw an error

#set operations

x={'a','b','c'}
y={'c','d'}
print('a'in x)
print(x|y)#union
print(x&y)#intersection
print(x-y)