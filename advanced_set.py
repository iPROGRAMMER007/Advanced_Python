
#empty set
s = set()
print(s)

s.add(1)
s.add(2)
s.add(3)
s.add(2)


s_copy = s.copy()

s_copy.add(56)
s_copy.add(78)
s_copy.add(90)

s_diff = s_copy.difference(s)

st = {11,22,34,56}
st.add(2)
st.add(3)
print(st)


#print(s_diff)
#print(s_copy)
print(s)

s_union = s.union(st)
print(s_union)

s_inter_section = s.intersection(st)
print(s_inter_section)








