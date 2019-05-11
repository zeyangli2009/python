print('the first triangle:')
for i in range(10):
    print(i*'*')
print('the second triangle:\n')
for i in range(10):
    print((10-i)*'*')
print('the third triangle:\n')    
i=1
while (i<10):
    print(i*'6')
    i = i + 1
print('the forth triangle:\n') 
for i in range(10):
    print((10-i)*'0')

print('the fifth triangle:\n') 
for i in range(10):
    print(i*' '+ (10-i)*'0')

print('the sixth triangle:\n')  
for i in range(100):
    print(i*' '+(100-i))          