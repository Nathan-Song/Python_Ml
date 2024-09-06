

# file 1
class CurrentUser:
    _instance = None

    name = "empty"
    age = 10

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CurrentUser, cls).__new__(cls)
        return cls._instance


class CurrentSettings:
    _instance = None

    dark_mode = True
    background_color = "Yellow"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CurrentSettings, cls).__new__(cls)
        return cls._instance


# file 2
user = CurrentUser()


settings = CurrentSettings()
settings.background_color = "red"

settings_2 = CurrentSettings()
print(settings_2.background_color == settings.background_color)
