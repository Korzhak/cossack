from manager.os_manager import OS
from manager.config_parser import Config

class Shell(OS):
    def __init__(self):
        self.config = Config()

    def command(self, cmd: str):
        is_sudo = False
        sudo_start = cmd.find("sudo")

        if sudo_start != -1:
            is_sudo = True
            cmd = cmd[5:]
        self.runner(f"{self.sudo(self.config.os.sudo_password) if is_sudo else ''} {cmd}")




