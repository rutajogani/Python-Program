string = """my favorite car is bmw.
my favorite fruit is mango.
my favorite game is badminton."""
txt = "hello, world!"
my_tuple = ("apple","banana","mango")

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