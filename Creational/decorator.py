import functools


def simple_decorator(func):
    @functools.wraps(func)
    def simple_wrapper(*args, **kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        try:
            func(*args)
        except Exception as err:
            print(err, ' --> Use kwargs instead')
            func(**kwargs)
    return simple_wrapper


@simple_decorator
def hello(name):
    """Hello to someone"""
    print('Hello {}\n'.format(name))


def advance_decorator(*args1, **kwargs1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args2, **kwargs2):
            print('The positional arguments of decorator are: ', args1)
            print('The keyword arguments of decorator are: ', kwargs1)
            print('The positional arguments of passing function are: ', args2)
            print('The keyword arguments of passing function are: ', kwargs2)
            func(*args2, **kwargs2)

        return wrapper

    return decorator


@advance_decorator('Nigga', 'Black', 'Basketball')
def goodbye(name, location='VietNam', time='Monday'):
    """Goodbye to someone"""
    print('Goodbye {} of {} on {}'.format(name, location, time))


if __name__ == '__main__':
    hello('Tien')
    hello(name='Tien')
    print('Name: ', hello.__name__, '\nDoc: ', hello.__doc__, '\n')
    goodbye('Tien', time='Wednesday')
    print('Name: ', goodbye.__name__, '\nDoc: ', goodbye.__doc__, '\n')
