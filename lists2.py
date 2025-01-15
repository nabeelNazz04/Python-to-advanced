courses=["Phy","Mat","Chemm","Bio","Hin"]
for index,course in enumerate(courses,start=1):#accessing values and index using enumerate function
  print(index,course)
course_str=", ".join(courses)#to make our list seperated by ,
new_list=course_str.split(", ")
print(course_str)
print(new_list)

#list vs tuple([]vs ())
#list is mutable and tuple is immutable
list_1=[1,2,3,4]
list_2=list_1
print(list_1)
print(list_2)
list_2[0]=10
print(list_1)
print(list_2)

tuple_1=(1,2,3,4)
tuple_2=tuple_1
print(tuple_1)
print(tuple_2)
#tuple_1[0]=8 throws error so tuple is immutable
print(tuple_1)
print(tuple_2)

#sets
set_1={"Phy","Mat","Chemm","Bio","Hin","Mat"} #set doesnot follow order,doesnot allow repitition
set_2={"Art","Chemm","Hin"}
print(set_1)
print("Mat"in set_1)
print(set_1.intersection(set_2))
print(set_1.difference(set_2))
print(set_1.union(set_2))