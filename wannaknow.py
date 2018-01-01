import curses
import time
from curses import wrapper
from stats import getStats
from renders import proc_row, conn_row, usr_row
from renders import pck_row, usr_head, proc_head, pck_head

def main(stdscr):

    # Clear screen
    stdscr.clear()
    # Curses Settings // DO NOT CHANGE
    curses.curs_set(False)
    stdscr.nodelay(True)
    # stdscr.idlok(1)
    # stdscr.scroll()

    # title = stats['title']
    black = curses.COLOR_BLACK
    curses.init_pair(1, curses.COLOR_WHITE, black)
    curses.init_pair(2, curses.COLOR_RED, black)
    curses.init_pair(3, curses.COLOR_GREEN, black)
    curses.init_pair(4, curses.COLOR_BLUE, black)
    curses.init_pair(5, curses.COLOR_YELLOW, black)
    curses.init_pair(6, curses.COLOR_CYAN, black)
    curses.init_pair(7, curses.COLOR_MAGENTA, black)

    curses.init_pair(8, curses.COLOR_BLUE, curses.COLOR_WHITE)

    while True:
        stats = getStats()
        stdscr.clear() # Dont Change!
        curses.flushinp() # Dont Change!

        term_size = stdscr.getmaxyx()

        term_1 = stdscr.subwin(term_size[0], 58, 0, 0)
        curr = term_1.getyx()
        col_2 = (curr[0], curr[1] + 7)
        col_3 = (curr[0], curr[1] + 21)
        col_4 = (curr[0], curr[1] + 31)
        col_5 = (curr[0], curr[1] + 47)

        usr_head(term_1, col_2, col_3, col_4, col_5, 4)

        for c in range(0, len(stats['users'])):
            user = stats['users'][c]

            curr = term_1.getyx()
            col_2 = (curr[0], curr[1] + 11)
            col_3 = (curr[0], curr[1] + 24)
            col_4 = (curr[0], curr[1] + 33)
            col_5 = (curr[0], curr[1] + 50)

            usr_row(term_1, user, col_2, col_3, col_4, col_5, 3, 1)

        # Network Info Display (Packets)
        curr = term_1.getyx()
        col_2 = (curr[0], curr[1] + 7)

        pck_head(term_1, 8, 4)

        interfaces = stats['network']['interfaces']
        for i in range(len(interfaces.items())):
            curr = term_1.getyx()
            col_2 = (curr[0], curr[1] + 10)
            pck_row(term_1, interfaces, col_2, i, 3, 2)

        # (Established Connections)
        curr = term_1.getyx()
        col_2 = (curr[0], curr[1] + 7)

        # estb_connections = stats['network']['connections']['established']
        # lstn_connections = stats['network']['connections']['listening']
        connections = stats['network']['connections']

        num_connects = len(connections.items())
        h = term_size[0] - curr[0]
        if h > num_connects:
            h = num_connects

        #TODO make a non-displayed dict of items in case of overflow
        # k = stdscr.getch()
        # if num_connects > term_size[0] - curr[0]:


        row = 0
        term_1.addstr('\nNETWORK CONNECTIONS\n', curses.color_pair(4) | curses.A_BOLD)

        for c in range(curr[0], h):
            cur = term_1.getyx()
            col_2 = (cur[0], cur[1] + 7)
            col_3 = (cur[0], cur[1] + 26)
            col_4 = (cur[0], cur[1] + 35)

            conn_row(term_1, connections, col_2, col_3, col_4, row, 3, 1, 4, 5)
            row += 1

        term_1.refresh()

        #Processes
        term_2 = stdscr.subwin(term_size[0], 60, 0, 58)

        curr = term_2.getyx()
        col_2 = (curr[0], curr[1] + 6)
        col_3 = (curr[0], curr[1] + 35)

        proc_head(term_2, col_2, col_3, 7, 8)

        o_procs = stats['processes']['other']

        curr = term_2.getyx()
        num_o_procs = len(stats['processes']['other'].items())

        row = 0
        for c in range(curr[0], term_size[0] - 1):
            curr = term_2.getyx()
            col_2 = (curr[0], curr[1] + 6)
            col_3 = (curr[0], curr[1] + 35)
            col_4 = (curr[0], curr[1] + 50)

            if o_procs[row]['user'] == 'root':
                proc_row(term_2, o_procs, col_2, col_3, col_4, row, 2)

            elif o_procs[row]['user'] == stats['users'][0]['name']:
                proc_row(term_2, o_procs, col_2, col_3, col_4, row, 6)

            else:
                proc_row(term_2, o_procs, col_2, col_3, col_4, row, 5)
            row += 1

        term_2.refresh()

        term_3 = stdscr.subwin(term_size[0], 60, 0, 116)

        curr = term_3.getyx()
        col_2 = (curr[0], curr[1] + 6)
        col_3 = (curr[0], curr[1] + 35)

        proc_head(term_3, col_2, col_3, 7, 8)

        curr = term_3.getyx()
        h = term_size[0] - 1
        remains = num_o_procs - row

        if h > remains:
            h = remains
        for a in range(curr[0], h):
            curr = term_3.getyx()
            col_2 = (curr[0], curr[1] + 6)
            col_3 = (curr[0], curr[1] + 35)
            col_4 = (curr[0], curr[1] + 50)

            if o_procs[row]['user'] == 'root':
                proc_row(term_3, o_procs, col_2, col_3, col_4, row, 2)

            elif o_procs[row]['user'] == stats['users'][0]['name']:
                proc_row(term_3, o_procs, col_2, col_3, col_4, row, 6)
            else:
                proc_row(term_3, o_procs, col_2, col_3, col_4, row, 5)
            row += 1

            # term_3.noutrefresh()
        term_3.refresh()

        # stdscr.addstr(c, 60, 'APPLE\n', curses.color_pair(3))
        # c = c + 1
        # a_procs = stats['processes']['apple']
        # for a in range(0, len(a_procs.items())):
        #     # parent = a_procs[a]['parent']
        #     proc = str( a_procs[a]['pid']) + '    ' + a_procs[a]['name'] + '    ' + \
        #             str(a_procs[a]['user']) + '    ' + str(a_procs[a]['parent'])
        #     stdscr.addstr(c, 60, proc + '\n', curses.color_pair(1))
        #     c += 1


        #DO NOT CHANGE BELOW THIS LINE
        # stdscr.refresh()
        # ###stdscr.getkey()
        time.sleep(0.5)

wrapper(main)
