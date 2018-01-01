import psutil, sched, time, sys

from system_info import getUserDetails
from network import getConnections, packetSniff
from proc_infos import getProcesses

def getStats():
    try:
        stats = {}
        stats['title'] = 'Wanna Know ?'.upper()
        stats['users'] = getUserDetails()

        network = {}
        network['connections'] = getConnections()
        network['interfaces'] = packetSniff()

        stats['network'] = network
        stats['processes'] = getProcesses()

        return stats

    except Exception as e:
        pass

# This other main function can be commented out for debugging purposes when there seems
# to be an issue with gathering the data

# def main():
    # try:
        #Create a scheduler instance
        # schedule = sched.scheduler(
        #     timefunc=time.time, delayfunc=time.sleep)

    # stats = {}

    # stats['title'] = 'Wanna Know ?'
    # stats['users'] = getUserDetails()
    #
    # network = {}
    # network['connections'] = getConnections()
    # network['interfaces'] = packetSniff()
    #
    # stats['network'] = network
    # stats['processes'] = getProcesses()
    # stats = getStats()
    #
    # print('\n<--- Users Connected--->\n')
    # print(stats['users'])
    #     # for u in users:
    #     #     print(u)
    #     #
    #
    #
    # print('\n<--- Network Connections --->\n')
    # print(stats['network']['connections'])
    #     # for c in connections:
    #     #     print(c)
    #     #
    #
    # print('\n<--- Interfaces --->\n')
    # print(stats['network']['interfaces'])
        # for p in packets:
        #     print(p)
        #
        # print('\n<--- Running Processes --->\n')
        # print('<--- General --->\n')
        # print(stats['processes']['other'])
        # # for p in processes[0]:
        # #     print(p)
        # print('\n<--- Apple --->\n')
        # print(stats['processes']['apple'])
        # # for p in processes[1]:
        # #     print(p)

    # except Exception as e:
        # print(e)
        # exit(1)


# if __name__ == "__main__":
#     main()
