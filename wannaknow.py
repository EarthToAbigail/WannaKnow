import curses
import time, sys
from math import floor
from curses import wrapper
from stats import getStats
from renders import proc_row, conn_row, usr_row, pck_row
from renders import usr_head, proc_head, pck_head, net_head, usage

def main(stdscr):

    # Clear screen
    stdscr.clear()
    # Curses Settings // DO NOT CHANGE
    curses.curs_set(False)
    stdscr.nodelay(True)

    black = curses.COLOR_BLACK
    curses.init_pair(1, curses.COLOR_WHITE, black)
    curses.init_pair(2, curses.COLOR_RED, black)
    curses.init_pair(3, curses.COLOR_GREEN, black)
    curses.init_pair(4, curses.COLOR_BLUE, black)
    curses.init_pair(5, curses.COLOR_YELLOW, black)
    curses.init_pair(6, curses.COLOR_CYAN, black)
    curses.init_pair(7, curses.COLOR_MAGENTA, black)

    curses.init_pair(8, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(9, black, curses.COLOR_BLUE)

    while True:
        try:
            stats = getStats()

            try:
                users = stats['users']
                interfaces = stats['network']['interfaces']
                connections = stats['network']['connections']
                procs = stats['processes']
            except TypeError:
                pass

            stdscr.clear() # Dont Change!

            # Define section specific variables
            num_connects = len(connections.items())
            num_closed = 0
            for i in range(0, num_connects):
                if connections[i]['status'] == 'CLOSE_WAIT':
                    num_closed += 1

            num_procs = len(procs.items())

            # Manipulate row numbers according to user input
            try:
                row_conn
            except NameError:
                row_conn = 0

            try:
                row_proc
            except NameError:
                row_proc = 0

            k = stdscr.getch()

            if k == ord('a'):
                if num_connects > connect_height:
                    row_conn = connect_height
                curses.flushinp()

            elif k == ord('s'):
                if num_connects > connect_height * 2:
                    row_conn = connect_height * 2
                curses.flushinp()

            elif k == ord('d'):
                if num_connects > connect_height * 3:
                    row_conn = connect_height * 3
                curses.flushinp()

            elif k == ord('w'):
                if num_connects > connect_height * 4:
                    row_conn = connect_height * 4
                curses.flushinp()

            elif k == ord('z'):
                if num_connects > connect_height * 5:
                    row_conn = connect_height * 5
                curses.flushinp()

            elif k == ord('x'):
                row_conn = 0
                curses.flushinp()

            elif k == ord('j'):
                if num_procs >= term_size[0] * 2 - 2:
                    row_proc = term_size[0] * 2 - 4
                curses.flushinp()

            elif k == ord('k'):
                if num_procs >= term_size[0] * 4 - 2:
                    row_proc = term_size[0] * 4 - 8
                curses.flushinp()

            elif k == ord('l'):
                if num_procs >= term_size[0] * 6 - 2:
                    row_proc = term_size[0] * 6 - 12
                curses.flushinp()

            elif k == ord('i'):
                if num_procs >= term_size[0] * 8 - 2:
                    row_proc = term_size[0] * 8 - 16
                curses.flushinp()

            elif k == ord('m'):
                if num_procs >= term_size[0] * 10 - 2:
                    row_proc = term_size[0] * 10 - 20
                curses.flushinp()

            elif k == ord('b'):
                row_proc = 0
                curses.flushinp()

            # Define max width and height
            try:
                term_size
            except NameError:
                term_size = stdscr.getmaxyx()

            resized = curses.is_term_resized(term_size[0], term_size[1])

            # Recalculate if terminal has been resized
            if resized == True:
                term_size = stdscr.getmaxyx()

            # Create sub-windows
            win_width = term_size[1] / 3

            term_1 = stdscr.subwin(term_size[0], floor(win_width) - 2, 0, 0)
            term_2 = stdscr.subwin(term_size[0], floor(win_width), 0, floor(win_width) - 3)
            term_3 = stdscr.subwin(term_size[0], floor(win_width), 0, floor(win_width * 2) - 3)

            # Left column of terminal screen (term_1)
            curr = term_1.getyx()

            col_2 = (curr[0], curr[1] + (floor(win_width/5)) - 5)
            col_3 = (curr[0], curr[1] + (floor((win_width/5)*2)) - 4)
            col_4 = (curr[0], curr[1] + (floor((win_width/5)*3)) - 7)
            col_5 = (curr[0], curr[1] + (floor((win_width/5)*4)) - 3)

            usr_head(term_1, col_2, col_3, col_4, col_5, 4)

            for c in range(0, len(users.items())):
                user = users[c]

                curr = term_1.getyx()

                col_2 = (curr[0], curr[1] + (floor(win_width/5)) - 2)
                col_3 = (curr[0], curr[1] + (floor((win_width/5)*2)) - 1)
                col_4 = (curr[0], curr[1] + (floor((win_width/5)*3)) - 5)
                col_5 = (curr[0], curr[1] + floor((win_width/5)*4))

                usr_row(term_1, user, col_2, col_3, col_4, col_5, 3, 1)

            # Network Info Display (Packets)
            curr = term_1.getyx()
            col_2 = (curr[0], curr[1] + floor(win_width/5))

            # Save the current location as coordinates to print the usage later on.
            col_instruct = (col_2[0] + 1, col_2[1] + floor((win_width/5))*2 - 3)

            pck_head(term_1, col_2, 8, 4, win_width)

            for i in range(0, len(interfaces.items())):
                curr = term_1.getyx()

                col_2 = (curr[0], curr[1] + floor(win_width/5))
                pck_row(term_1, interfaces, col_2, i, 3, 2)

            net_head(term_1, num_connects, num_closed)

            curr = term_1.getyx()
            connect_height = term_size[0] - curr[0] - 1
            col_2 = (curr[0], curr[1] + (floor(win_width/5)) - 5)

            if row_conn > 0:
                row_c = row_conn
            else:
                row_c = 0

            h1 = term_size[0] - 1

            for c in range(curr[0], h1):
                if row_c == num_connects:
                    break
                cur = term_1.getyx()
                col_2 = (cur[0], cur[1] + (floor(win_width/5)) - 4)
                col_3 = (cur[0], cur[1] + (floor((win_width/5)*2)) + 3)
                col_4 = (cur[0], cur[1] + (floor((win_width/5)*3)) - 1)

                conn_row(term_1, connections, col_2, col_3, col_4, row_c, 3, 1, 4, 5, 9)
                row_c += 1

            # Print usage instructions
            usage(term_1, col_instruct)

            term_1.refresh()

            # Middle column of terminal screen (term_2)
            #Processes
            curr = term_2.getyx()
            col_2 = (curr[0], curr[1] + (floor(win_width/5)) - 5)
            col_3 = (curr[0], curr[1] + (floor((win_width/5)*3)))

            proc_head(term_2, col_2, col_3, 7, 8)

            curr = term_2.getyx()

            if row_proc > 0:
                row_p = row_proc
            else:
                row_p = 0

            h2 = term_size[0] - 1

            for c in range(curr[0], h2):
                if row_p == num_procs:
                    break
                curr = term_2.getyx()
                col_2 = (curr[0], curr[1] + (floor(win_width/5)) - 6)
                col_3 = (curr[0], curr[1] + (floor((win_width/5)*3)))
                col_4 = (curr[0], curr[1] + (floor((win_width/5)*4)) + 3)

                if procs[row_p]['user'] == 'root':
                    proc_row(term_2, procs, col_2, col_3, col_4, row_p, 2)

                elif procs[row_p]['user'] == users[0]['name']:
                    proc_row(term_2, procs, col_2, col_3, col_4, row_p, 6)

                else:
                    proc_row(term_2, procs, col_2, col_3, col_4, row_p, 5)
                row_p += 1

            term_2.refresh()

            # Right column of terminal screen (term_3)
            curr = term_3.getyx()
            col_2 = (curr[0], curr[1] + (floor(win_width/5)) - 5)
            col_3 = (curr[0], curr[1] + (floor((win_width/5)*3)))

            proc_head(term_3, col_2, col_3, 7, 8)

            curr = term_3.getyx()

            h3 = term_size[0] - 1

            for a in range(curr[0], h3):
                if row_p == num_procs:
                    break
                curr = term_3.getyx()
                col_2 = (curr[0], curr[1] + (floor(win_width/5)) - 6)
                col_3 = (curr[0], curr[1] + (floor((win_width/5)*3)))
                col_4 = (curr[0], curr[1] + (floor((win_width/5)*4)) + 3)

                if procs[row_p]['user'] == 'root':
                    proc_row(term_3, procs, col_2, col_3, col_4, row_p, 2)

                elif procs[row_p]['user'] == users[0]['name']:
                    proc_row(term_3, procs, col_2, col_3, col_4, row_p, 6)
                else:
                    proc_row(term_3, procs, col_2, col_3, col_4, row_p, 5)
                row_p += 1

            term_3.refresh()

            time.sleep(0.2)

        except KeyboardInterrupt:
            return sys.exit('Thank you! Goodbye!')

try:
    wrapper(main)
except TypeError:
    sys.exit('"Are you using python3?"\n')
except Exception:
    sys.exit('"If you don\'t have root privileges, I can\'t help you!"\n')
