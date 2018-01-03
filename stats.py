import psutil, sys

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
# to be an issue with gathering the data, needs to be adjusted to the debugging purpose.

# def main():
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

    #
    # print('\n<--- Network Connections --->\n')
    # print(stats['network']['connections'])

    #
    # print('\n<--- Interfaces --->\n')
    # print(stats['network']['interfaces'])

    # print('\n<--- Running Processes --->\n')
    # print('<--- General --->\n')
    # print(stats['processes']['other'])
    # # for p in processes[0]:
    # #     print(p)
    # print('\n<--- Apple --->\n')
    # print(stats['processes']['apple'])


# if __name__ == "__main__":
#     main()
