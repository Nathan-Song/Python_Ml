

def check_status(get_profile):

    def wrapper(user_id):
        if user_id == 10:
            print("Allowed to get profile:")
        else:
            raise ValueError("Not allowed")

        res = get_profile(user_id)
        print("Sent user profile to: ", user_id)

        return res

    return wrapper


@check_status
def get_profile(user_id):
    return {"id": user_id, "name": "Test Name"}


def get_posts(user_id):
    return {"id": user_id, "name": "Test Name"}


@check_status
def get_name(user_id):
    return {"id": user_id, "name": "Test Name"}


@check_status
def get_est(user_id):
    return {"id": user_id, "name": "Test Name"}


print(get_profile(10))


# def get_profile(user_id):
#     check_if_allowed(user_id)
#     print("Get Profile")
#     send_user_profile(user_id)


# def check_if_allowed(user_id):
#     print("Allowed to get profile:", user_id)


# def send_user_profile(user_id):
#     print("Sent user profile to: ", user_id)


# get_profile(10)
