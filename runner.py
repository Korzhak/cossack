import sys
from manager import run
from dispatches import UTILS_DISPATCHES


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "createuser":
            from manager.db_manager.create_user import create_user
            create_user()
        elif sys.argv[1] == "createdb":
            from manager.db_manager.manager import create_db
            create_db()
        else:
            print(f"Unexpected command {sys.argv[1]}")

    else:
        run(UTILS_DISPATCHES)

