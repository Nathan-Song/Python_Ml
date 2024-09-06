
def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

# file 1


@singleton
class CurrentUser:
    name = "empty"
    age = 10


@singleton
class CurrentSettings:
    dark_mode = True
    background_color = "Yellow"


# file 2
user = CurrentUser()


settings = CurrentSettings()
settings.background_color = "red"

settings_2 = CurrentSettings()
print(settings_2.background_color == settings.background_color)
