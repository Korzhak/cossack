from telegram.ext import CommandHandler, RegexHandler, CallbackQueryHandler
from .commands import *
from .nginx import Nginx

nx = Nginx()

dispatches = [
    RegexHandler(NGINX, nx.nginx_menu),

    RegexHandler(RESTART_NGINX, nx.restart_nginx),
    RegexHandler(START_NGINX, nx.start_nginx),
    RegexHandler(STOP_NGINX, nx.stop_nginx),

    RegexHandler(STATUS_NGINX, nx.status_nginx),

    RegexHandler(GET_AVAILABLE_HOST, nx.get_available_hosts),
    RegexHandler(GET_ENABLED_HOST, nx.get_enabled_hosts),
    

    RegexHandler(MANAGE_HOST, nx.manage_host),
    RegexHandler(ENABLING_HOST, nx.enabling_host_menu),
    RegexHandler(DISABLING_HOST, nx.disabling_host_menu),
    
]