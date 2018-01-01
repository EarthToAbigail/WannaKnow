import psutil, sys


def getConnections():
    """ Returns an array of arrays representing the local and foreign ips and ports
        of established and listening connections as well as their pid. """

    c = psutil.net_connections()
    connects = {}
    # established =  {}
    # listen = {}
    # e = 0
    # l = 0
    count = 0
    for connection in c:
        conn = {}
        status = connection.status
        if status == 'ESTABLISHED':
            conn['status'] = status
            conn['local'] = connection.laddr[0] + ':' + str(connection.laddr[1])
            conn['remote'] = connection.raddr[0] + ':' + str(connection.raddr[1])
            # established[e] = conn
            connects[count] = conn
            # e += 1
            count += 1
        elif connection.status == 'LISTEN':
            conn['status'] = status
            conn['local'] = connection.laddr[0] + ':' + str(connection.laddr[1])
            connects[count] = conn
            count += 1
        else:
            # print(connection.status)
            pass

    # connects['established'] = established
    # connects['listening'] = listen
    return connects

def packetSniff():
    """ Returns only active interfaces that are sending or receiving packets """

    packets = psutil.net_io_counters(pernic=True)
    interfaces = {}
    x = 0
    for p in packets.items():
        values = {}
        # name = p[0]
        values['name'] = p[0]
        values['bytes_sent'] = p[1][0]
        values['bytes_recv'] = p[1][1]
        values['pckt_sent'] = p[1][2]
        values['pckt_recv'] = p[1][3]
        values['errin'] = p[1][4]
        values['errout'] = p[1][5]
        values['dropin'] = p[1][6]
        values['dropout'] = p[1][7]
        if ((values['bytes_sent'] or values['bytes_recv'] or values['pckt_sent'] or values['pckt_recv']) != 0):
            interfaces[x] = values
            x += 1
        else:
            pass

    return interfaces
