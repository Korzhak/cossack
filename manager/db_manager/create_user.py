from manager.db_manager.manager import add_user


def create_user():
    user_id = int(input("Telegram user id (/get_my_id command in bot): "))
    pin_code = int(input("Pin code for access to secured functions: "))
    session_duration = int(input("in msec. 1800 sec (30 min): "))

    add_user(user_id, pin_code, 1, session_duration)


def update_user():
    user_id = int(input("Telegram user id (/get_my_id command in bot): "))
    pin_code = int(input("Pin code for access to secured functions: "))
    session_duration = int(input("in msec. 1800 sec (30 min): "))

    add_user(user_id, pin_code, 1, session_duration)


def delete_user():
    user_id = int(input("Telegram user id (/get_my_id command in bot): "))

    add_user(user_id)