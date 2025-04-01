try:
    print(5/0)
except ZeroDivisionError:
    print('hello world!')
except ModuleNotFoundError:
    print("mwahahahahh")
print("you'll never know")

while True:
    no_1 = input('first number: ')
    if no_1 == 'q':
        break
    no_2 = input('first number: ')
    if no_2 == 'q':
        break
    try:
        result = int(no_1)/int(no_2)
    except ZeroDivisionError:
        print('cannot divide by zero')
    except ValueError:
        print('That\'s not a number')
    except:
        print('you\'ll never know')
    else:
        print(f'result is {result}')