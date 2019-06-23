from manager.os_manager import OS
from manager import config


class NginxManager(OS):
    def start(self):
        cmd = f"{self.sudo(config.os.sudo_password)}{self.service('nginx', 'start')}"
        return self.runner(cmd)

    def restart(self):
        cmd = f"{self.sudo(config.os.sudo_password)}{self.service('nginx', 'restart')}"
        return self.runner(cmd)

    def stop(self):
        cmd = f"{self.sudo(config.os.sudo_password)}{self.service('nginx', 'stop')}"
        return self.runner(cmd)

    def status(self):
        cmd = f"{self.sudo(config.os.sudo_password)}{self.service('nginx', 'status')}"
        return self.runner(cmd, return_result=True)

    def get_enabled_hosts(self, user_id):
        return self.ls(user_id=user_id, path="/etc/nginx/sites-enabled/")

    def get_available_host(self, user_id):
        return self.ls(user_id=user_id, path="/etc/nginx/sites-available/")

    def enabling_host(self, name_file):
        cmd = f'{self.sudo(config.os.sudo_password)} ln -s ' \
              f'/etc/nginx/sites-available/{name_file} /etc/nginx/sites-enabled/'
        return self.runner(cmd)

    def disabling_host(self, name_file):
        cmd = f'{self.sudo(config.os.sudo_password)} rm ' \
              f'/etc/nginx/sites-enabled/{name_file}'
        return self.runner(cmd)

    def __str__(self):
        return self.status()

    def __call__(self, *args, **kwargs):
        return self.start()

