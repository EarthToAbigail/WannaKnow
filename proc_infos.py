import psutil, sys

def getProcesses():
    """ Returns running processes grouped by apple and other identified """
    pids = psutil.pids()
    processes = {}
    apple = {}
    other = {}
    a = 0
    o = 0
    for p in pids:
        proc = psutil.Process(p)
        process = {}
        process['name'] = proc.name()
        process['user'] = proc.username()
        process['pid'] = p
        parent = {}
        prt = proc.parent()
        parent['pid'] = prt.pid
        parent['name'] = prt.name()
        process['parent'] = parent

        if proc.status() == 'running':
            if 'apple' in process['name']:
                apple[a] = process
                a += 1
            else:
                other[o] = process
                o += 1

    processes['apple'] = apple
    processes['other'] = other

    return processes
