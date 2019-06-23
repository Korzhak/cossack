from plugins.home.dispatches import dispatches as home_dispatches
from plugins.nginx.dispatches import dispatches as nginx_dispatches
from plugins.shell.dispatches import dispatches as shell_dispatches

UTILS_DISPATCHES = [
    nginx_dispatches,
    home_dispatches,
    shell_dispatches,
]




