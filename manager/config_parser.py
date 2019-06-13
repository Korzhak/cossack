import configparser


class _BotConfig:
    def __init__(self, token):
        self.token = token


class _OSConfig:
    def __init__(self, sudo_user, sudo_password):
        self.sudo_user = sudo_user
        self.sudo_password = sudo_password


class Config:
    def __init__(self):
        self._config = configparser.ConfigParser()
        self._config_name = ''
        self._get_config()
        print(f"Read {self._config_name}")

        self.bot = _BotConfig(
            token=self._config['Bot_config']['bot_token'],
        )
        self.os = _OSConfig(
            sudo_user=self._config['OS_config']['sudo_user'],
            sudo_password=self._config['OS_config']['sudo_password'],
        )

    def _get_config(self):

        if self._config.read("local_config.ini"):
            self._config_name = "local_config.ini"

        elif self._config.read("config.ini"):
            self._config_name = "config.ini"

        else:
            print("Не знайдено жодного config.ini")

    # def update_config(self, is_auth, last_auth):
    #     self._config['Auth'] = {'is_auth': is_auth, 'last_auth': last_auth,
    #                             'session_duration': settings.SESSION_DURATION}
    #                             # 'session_duration': self.auth.session_duration}
    #
    #     with open(self._config_name, "w") as configure:
    #         self._config.write(configure)
    #
    #     self.auth.is_auth = is_auth

