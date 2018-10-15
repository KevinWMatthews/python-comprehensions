print('[x for x in range(10) if x > 0]')
result = [x for x in range(0, 10) if x > 0]
print(result)
print('')

print('[x for x in range(10)]')
result = [x for x in range(10)]
print(result)
print('')

print('[x for x in range(10) if x > 5]')
result = [x for x in range(10) if x > 5]
print(result)
print('')

print('[x**2 for x in range(10) if x % 2 != 0]')
result = [x**2 for x in range(10) if x % 2 != 0]
print(result)
print('')
