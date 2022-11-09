from Payman import calculate
def test(a,b):
    c=calculate(a,b)
    test_c=a+b
    assert c==test_c

test(10,45)
test(5,89)
test(89,90)