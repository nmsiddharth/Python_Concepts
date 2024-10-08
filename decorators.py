def new_decorator(func):
    def wrap_func():
        print("Some code before executing func")
        func()
        print("Some code after executing func")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("This function is in need of decorator")

func_needs_decorator()

            # OR

some_func = new_decorator(func_needs_decorator)
some_func()