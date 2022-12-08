try:
    number = int(input('enter number: '))
    print('Your number is -', number)
except:
    print('ValueError')

# блок "finaly"

try:
    a = int(input('enter number'))
    b = int(input('enter number'))
    print(a + b)
except:
    print('Fail, numbers must be integers')
finally:
    print('Program completion')
# 'finally' выполнится даже если исключение не сгенерировано

# try:
#     print(x)
# except:
#     print("An exception occurred")
