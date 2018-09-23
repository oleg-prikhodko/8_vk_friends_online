import sys
from getpass import getpass

import vk

APP_ID = 6700865


def get_user_login():
    return input("Enter your login: ")


def get_user_password():
    return getpass("Enter your password: ")


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope="friends",
    )
    api = vk.API(session, v="5.85", scope="friends")
    user_ids = api.friends.getOnline()
    user_infos = api.users.get(user_ids=user_ids)
    return user_infos


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print(friend["first_name"], friend["last_name"])


if __name__ == "__main__":
    vk.logger.disabled = True

    login = get_user_login()
    password = get_user_password()
    try:
        friends_online = get_online_friends(login, password)
        if not friends_online:
            print("No friends online")
        else:
            output_friends_to_console(friends_online)
    except vk.exceptions.VkException as vk_error:
        sys.exit(vk_error)
