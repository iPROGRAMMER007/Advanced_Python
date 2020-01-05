from collections import namedtuple

#Normal Tuple
t = (1,2,3,4)
print(t[2])

#Named tuple

family = namedtuple('family','first second third')

picnic_party = family(first='Irshad',second='Vikash',third='Chhota_Vikash')

print(picnic_party.first)
print(picnic_party.second)
print(picnic_party.third)











