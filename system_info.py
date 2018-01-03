import psutil, sys
import datetime

def getUserDetails():

    """ Return details on not only the user but also different sessions
        of the same user """

    u = psutil.users()
    users = {}
    x = 0
    for user in u:
        usr = {}
        usr['name'] = user.name
        usr['terminal'] = user.terminal
        usr['host'] = user.host
        usr['start'] = datetime.datetime.fromtimestamp(user.started).strftime('%Y-%m-%d %H:%M')[2:]
        usr['pid'] = user.pid
        users[x] = usr
        x += 1
    return users
