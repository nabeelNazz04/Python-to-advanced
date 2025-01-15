courses=["Phy","Mat","Chemm"]
print(courses.index("Phy"))#gives the index value
courses.insert(0,"Eng")
courses2=["skt","Hindi"]
#courses.insert(0,courses2)//[['skt', 'Hindi'], 'Eng', 'Phy', 'Mat', 'Chemm']
courses.extend(courses2)
courses.remove("Phy")
courses.pop()#pop the last value
courses.reverse()
courses.sort()
nums=[9,8,7,6,5,4,3]
nums.sort()
print(courses)
print(nums)
nums.sort(reverse=True)
courses.sort(reverse=True)
print("Reversed:")
print(nums)
print(courses)

#to get a sorted version without altering the orignal
sorted_version=sorted(nums)
print(sorted_version)
print(nums)