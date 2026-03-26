from FixedPoint import FXfamily, FXnum

x = FXnum(22) / FXnum(7)
y = FXnum(3.1415)

print("x =", x)
print("y =", y)
print("x - y =", x - y)

fam16 = FXfamily(16)
a = FXnum(1.5, fam16)
b = FXnum(2.25, fam16)

print("a =", a)
print("b =", b)
print("a + b =", a + b)
print("a * b =", a * b)
print("sqrt(b) =", b.sqrt())
print("pi =", fam16.pi)