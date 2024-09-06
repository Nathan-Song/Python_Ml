

def logging(cls):
    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value):

            def create_a_func(attr_name, attr_value):

                def logged_method(self, *args, **kwargs):
                    print(f"Calling {attr_name}" +
                          f" with args: {args}, kwargs: {kwargs}")
                    return attr_value(self, *args, **kwargs)

                return logged_method

            setattr(cls, attr_name, create_a_func(attr_name, attr_value))

            # setattr(cls, attr_name, logged_method)

    return cls


@logging
class Math:

    def double(self, x):
        pdb.set_trace()
        return x * 2

    def half(self, x):
        return x / 2


math = Math()

print(math.double(2))
print(math.half(4))
