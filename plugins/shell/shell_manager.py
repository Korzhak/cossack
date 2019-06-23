from manager.os_manager import OS
from manager import config


class Shell(OS):

    def command(self, cmd: str):
        is_sudo = False
        sudo_start = cmd.find("sudo")

        if sudo_start != -1:
            is_sudo = True
            cmd = cmd[5:]
        self.runner(f"{self.sudo(config.os.sudo_password) if is_sudo else ''} {cmd}")
