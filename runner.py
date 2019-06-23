import sys


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "createuser":
            from manager.db_manager.create_user import create_user
            create_user()
        elif sys.argv[1] == "createdb":
            from manager.db_manager import create_db
            create_db()
        else:
            print(f"Unexpected command {sys.argv[1]}")

    else:
        from dispatches import UTILS_DISPATCHES
        from manager import run

        run(UTILS_DISPATCHES)

