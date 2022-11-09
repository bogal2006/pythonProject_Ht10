from main.py import calculate as cal
def test(a,b):
    c=cal(a,b)

test_c=a+b
assert c==test_c

test(10,45)
test(-5,89)
test_c(89,90)