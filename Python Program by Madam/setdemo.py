lst1=[12,13,16,34,7,5,12,45,16]
s=set(lst1)
print(s)
lst2=[13,16,2,3,5,18,13,16,3,5,3]
s1=set(lst2)
print(s1)
##print(s.union(s1))
##print(s|s1)
##print(s.intersection(s1))
##print(s&s1)
print(s.difference(s1))
print(s-s1)
s=s-s1
print(s.difference_update(s1))
if s<s1:
    print("it is subset")
else:
    print("it is superset")
if s>s1:
    print("it is superset")
else:
    print("it is subset....................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................0........................................................................................................................................................................................................................

          ")

