from square import Square as sq
from traingle import Triangle as tq

s1 = sq()
s1.set_value(8, 15)
s1.set_color("Blue")
print(s1.area(), s1.get_color())

t1 = tq()
t1.set_value(5, 10)
t1.set_color("Green")
print(t1.area(), t1.get_color())
