from plugins.nginx.dispatches import dispatches as nginx_dispatches
from plugins.home.dispatches import dispatches as home_dispatches

UTILS_DISPATCHES = [
    nginx_dispatches,
    home_dispatches,
]




