#### decorater using @



def validate_user(func):                                            ## decorater
    def wrapper():
        name = input('Enter your name : ')
        paswd = input('Enter your password : ')
        if name == 'admin' and paswd == '123':
            func()
        else:
            print('Invalid credentials')
    return wrapper 


@validate_user
def deposit():
    print('money deposited')


deposit()