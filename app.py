### Python decorater


def deposit():
    print('money deposited')


def validate_user(func):
    def wrapper():
        name = input('Enter your name : ')
        paswd = input('Enter your password : ')
        if name == 'admin' and paswd == '123':
            func()
        else:
            print('Invalid credentials')
    return wrapper 

data = validate_user(deposit)

data()