s = "ajay jflsdfls jfkdsl jf dsfjlsdj lfdfkdsl  jlskdfldsf jflksd "
s1 = 'raj  fjkdsdlsjldfs'

s2 = ''' fkdsfls"
klsdjflsdk '
dljflds '
lkdsjfs '''

s3 = """ jdlkf dstreiouew 34093 rjlkjf "
dflsdj 
kjdslf 34345  """

# print(s1)
# print(s)


# your task is to find how to pass single quotes ' in between this string s= 'dfsd fds ' dfsd '


# slicing in python strin

naam = "Neev"

# # print(naam[0])
# print(naam[-1])
# # print(naam[1])
# print(naam[-4])
# print(naam * 5)


# naam = "Neev"

# print("o" in naam)
# print("o" not in naam)

# q = "Learnings"
# p = "Indore"
# q = "learning python is very very easy"
# print(q[: :3])
# print(q + p)

# print(len(p))


# removing spaces from string by 3 ways
# left - lstrip
# right - rstrip
# from both l and r - strip


# city = "##Hyderabad####"
# print(city.rstrip('#'))
# print(city.lstrip('#'))
# print(city.strip('#'))

#output : 
# '''###Hyderabad
# Hyderabad####
# Hyderabad'''



# s = "Nitya   is a very is smart boy"
# print(s1.find('d'))
# print(s.index('is a very'))


# m = "ababaab"
# print(m.count('a'))
# print(m.count('ab'))
# print(m.count('b',1,5))


# n = "Nitya   is a very is smart boy"
# t =n.replace('smart','handsome')
# print(t)


# m = " i am ajay"
# t= (m.replace('ajay','neev'))
# print(id(m))
# print(id(t))

# m = ' I am in mumbai right now'
# t = m.split('a')
# print(type(t))


# dattt= "10-oct-20-26"
# t = dattt.split('0')
# print(t)


# t = ('sunny','bunny','chinny')
# y = '+'.join(t)
# print(y)


s = "itya is a very is smart boy"
print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())
print(s.swapcase())

print(s.startswith('m'))
print(s.endswith('boys'))