# result = [... for ... if ... ]

# result = [10,20,30,40,50]


result = []

# for i in range(1, 5+1):
#     result.append(i * 10)

# print(result)

result = [i*10 for i in range(1, 5+1)]

print(result)

result = [i*10 for i in range(1, 5+1) if i % 2 == 0]
print(result)

result = [i*10  if i % 2 == 0 else 0 for i in range(1, 5+1)  ]
print(result)

result = [i*j for i in range(2, 5) for j in range(1,4)]
print(result)

