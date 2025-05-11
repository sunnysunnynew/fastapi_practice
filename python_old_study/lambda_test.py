def add(x,y):
    return x + y


add2 = add
print(add2(10,20))

results =(lambda x, y: x+y)(1,2)
print(results)

add3 = lambda x, y: x+y
print(add3(100,200))

lambda_list = [lambda x: x+10, lambda x: x+ 100]
print(lambda_list[0](5))

print(lambda_list[1](777))


add4 = lambda x,y: x+y
print(add4(1000,2000))
# add5 = lambda x: int, y: int : x+y (type hint.를 쓸 수 없다 )