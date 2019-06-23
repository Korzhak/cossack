from subprocess import *
from manager.db_manager.manager import update_bot_session, get_last_session

class OS:
    def runner(self, cmd, return_result=False):
        res = ''
        try:
            if not return_result:
                Popen(cmd, shell=True)
            else:
                res = check_output(cmd, shell=True)
        except Exception as e:
            return e.args
        else:
            if return_result:
                return res.decode("utf-8")
            return 0


    def sudo(self, password, run=False):
        cmd = f"echo {password} | sudo -S "
        if not run:
            return cmd
        return self.runner(cmd, return_result=True)


    def service(self, tool, action, run=False):
        cmd = f"service {tool} {action}"
        if not run:
            return cmd
        return self.runner(cmd, return_result=True)


    def ls(self, user_id: int, path: str = '', keys: str = '', run=True):
        session = get_last_session(id=user_id)
        cmd = ''
        if not path:
            cmd += f"ls {session.current_directory} {keys if keys else ''}"
        else:
            cmd += f"ls {path} {keys if keys else ''}"
        if not run:
            return cmd
        return self.runner(cmd, return_result=True)


    def pwd(self, user_id: int):
        session = get_last_session(id=user_id)
        return session.current_directory


    def cd(self, user_id: int, path: str):
        session = get_last_session(id=user_id)

        if path == ".." or path == "../":
            full_path = "/".join(session.current_directory.split("/")[:-1])

        elif path[0] != "/" and path[0] != "~":
            full_path = f"{session.current_directory}/{path}"

        else:
            full_path = path

        if not full_path:
            full_path = "/"

        cmd = f"cd {full_path}"

        self.runner(cmd, return_result=True)
        update_bot_session(id=user_id, path=full_path)


    def __str__(self):
        cmd = "uname -a"
        return str(self.runner(cmd, return_result=True))

    def __call__(self, *args, **kwargs):
        cmd = "uname -a"
        return str(self.runner(cmd, return_result=True))
