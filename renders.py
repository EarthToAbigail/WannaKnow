import curses

def proc_row(window, proc, col_2, col_3, col_4, idx, color):
    window.addstr(str(proc[idx]['pid']), curses.color_pair(color))
    window.addstr(col_2[0], col_2[1], str( proc[idx]['name']), curses.color_pair(color))
    window.addstr(col_3[0], col_3[1], str( proc[idx]['parent']['name']), curses.color_pair(color))
    window.addstr(col_4[0], col_4[1], str( proc[idx]['parent']['pid']) + '\n', curses.color_pair(color))

def conn_row(window, connection, col_2, col_3, col_4, idx, color1, color2, color3, color4):
    if connection[idx]['status'] == 'ESTABLISHED':
        window.addstr('ESTBL ', curses.color_pair(color1) | curses.A_BOLD)
        window.addstr(col_2[0], col_2[1], connection[idx]['local'], curses.color_pair(color2))
        window.addstr(col_3[0], col_3[1], '   ->   ', curses.color_pair(color3))
        window.addstr(col_4[0], col_4[1], connection[idx]['remote'] + '\n', curses.color_pair(color2))
    elif connection[idx]['status'] == 'LISTEN':
        window.addstr('LSTN ', curses.color_pair(color4) | curses.A_BOLD)
        window.addstr(col_2[0], col_2[1], connection[idx]['local'] + '\n', curses.color_pair(color2))

def usr_row(window, usr, col_2, col_3, col_4, col_5, color1, color2):
    window.addstr(str(usr['name']), curses.color_pair(color1) | curses.A_BOLD)
    window.addstr(col_2[0], col_2[1], str(usr['terminal']), curses.color_pair(color2))
    window.addstr(col_3[0], col_3[1], str(usr['host']), curses.color_pair(color2))
    window.addstr(col_4[0], col_4[1], str(usr['start']), curses.color_pair(color2))
    window.addstr(col_5[0], col_5[1], str(usr['pid']) + '\n', curses.color_pair(color2))

def pck_row(window, interface, col_2, idx, color1, color2):
    window.addstr(interface[idx]['name'], curses.color_pair(color1) | curses.A_BOLD)
    window.addstr(col_2[0], col_2[1], str(interface[idx]['pckt_sent']) + \
                    ' / ' + str(interface[idx]['pckt_recv']) + '\n',
                    curses.color_pair(color2) | curses.A_BOLD)

def usr_head(window, col_2, col_3, col_4, col_5, color):
    window.addstr("User  :", curses.color_pair(color) | curses.A_BOLD)
    window.addstr(col_2[0], col_2[1], ":  Terminal  :", curses.color_pair(color) | curses.A_BOLD)
    window.addstr(col_3[0], col_3[1], ":  Host  :", curses.color_pair(color) | curses.A_BOLD)
    window.addstr(col_4[0], col_4[1], ":  Start Time  :", curses.color_pair(color) | curses.A_BOLD)
    window.addstr(col_5[0], col_5[1], ":  PID\n", curses.color_pair(color) | curses.A_BOLD)

def proc_head(window, col_2, col_3, color1, color2):
    window.addstr('PID', curses.color_pair(color1) | curses.A_BOLD)
    window.addstr(col_2[0], col_2[1], 'Name', curses.color_pair(color2))
    window.addstr(col_3[0], col_3[1], 'Parent\n', curses.color_pair(color2))

def pck_head(window, color1, color2):
    window.addstr('\nInterface', curses.color_pair(color1))
    window.addstr(' PckSt / PckRecv\n', curses.color_pair(color2) | curses.A_BOLD)
