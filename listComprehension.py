list=[1,2,3,4,5,6,7]
even=[]
for i in list:
  if i%2==0:
    even.append(i)
print(even)

#doing this for one step is list comprehension

even = [i for i in list if i%2==0]
print(even)

sqr_numbers = [i*i for i in list]
print(sqr_numbers)

#for set
s=[1,1,2,2,3,4,4,5,6,6,7,8]
even={i for i in s if i%2==0}
print(even)

#dictionary comprehension
cities=['mumbai','california','elpaso']
countries=['India','America','Mexico']
z=zip(cities,countries)
print(z)
for i in z:
  print(i)
#comprehensed:

d={city:country for city,country in zip(cities,countries)}
print(d)