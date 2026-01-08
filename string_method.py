# string methods 

string = """my favorite car is bmw.
my favorite fruit is mango.
my favorite game is badminton."""

txt = "hello, world!"

my_tuple = ("apple","banana","mango")

new = "HELLO, GUYS!"

#length of string
print(len(string))
print("--------------------------")

#center with string
a = txt.center(20)
print(a)
print("--------------------------")

#count with string
b = string.count("favorite")
print(b)
print("--------------------------")

#join with two tuple
c = ",".join(my_tuple)
print(c)
print("--------------------------")

#replace string method
d = string.replace("my","jon's")
print(d)
print("--------------------------")

#lower method with string
e = new.lower()
print(e)
print("--------------------------")

#upper method with string
f = txt.upper()
print(f)
print("--------------------------")

#minimum method with string
g = [5, 10, 25, 2]
print(min(g))
print("--------------------------")

#maximum method with string
h = [5, 10, 25, 2]
print(max(h))
print("--------------------------")

