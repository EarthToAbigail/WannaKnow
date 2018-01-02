import psutil, sys

def getProcesses():
    """ Returns running processes grouped by apple and other identified """
    pids = psutil.pids()
    processes = {}

    count = 0
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
            processes[count] = process
            count += 1

    return processes
