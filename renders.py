import curses
from math import floor

def proc_row(window, proc, col_2, col_3, col_4, idx, color):
    window.addstr(str(proc[idx]['pid']), curses.color_pair(color))
    if 'apple' in proc[idx]['name']:
        name = str(proc[idx]['name']).split('apple')[1]
        window.addstr(col_2[0], col_2[1], ' ' + name, curses.color_pair(7) | curses.A_BOLD)
    else:
        window.addstr(col_2[0], col_2[1], ' ' + str( proc[idx]['name']), curses.color_pair(color) | curses.A_BOLD)

    window.addstr(col_3[0], col_3[1], str( proc[idx]['parent']['name']), curses.color_pair(1))
    window.addstr(col_4[0], col_4[1], str( proc[idx]['parent']['pid']) + '\n', curses.color_pair(1))

def conn_row(window, connection, col_2, col_3, col_4, idx, color1, color2, color3, color4, color5):
    if connection[idx]['status'] == 'ESTABLISHED':
        window.addstr('ESTBL ', curses.color_pair(color1) | curses.A_BOLD)
        window.addstr(col_2[0], col_2[1], connection[idx]['local'], curses.color_pair(color2) | curses.A_BOLD)
        window.addstr(col_3[0], col_3[1], '   ->   ', curses.color_pair(color3))
        window.addstr(col_4[0], col_4[1], connection[idx]['remote'] + '\n', curses.color_pair(color2) | curses.A_BOLD)

    elif connection[idx]['status'] == 'LISTEN':
        window.addstr('LSTN ', curses.color_pair(color4) | curses.A_BOLD)
        window.addstr(col_2[0], col_2[1], connection[idx]['local'] + '\n', curses.color_pair(color2))

    else:
        window.addstr('CL_WT', curses.color_pair(color3))
        window.addstr(col_2[0], col_2[1], connection[idx]['local'], curses.color_pair(color5))
        window.addstr(col_3[0], col_3[1], '   ->   ', curses.color_pair(color3))
        window.addstr(col_4[0], col_4[1], connection[idx]['remote'] + '\n', curses.color_pair(color5))

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
    window.addstr(col_4[0], col_4[1], ":  Start Time   :", curses.color_pair(color) | curses.A_BOLD)
    window.addstr(col_5[0], col_5[1], ":  PID\n", curses.color_pair(color) | curses.A_BOLD)

def proc_head(window, col_2, col_3, color1, color2):
    window.addstr('PID', curses.color_pair(color1) | curses.A_BOLD)
    window.addstr(col_2[0], col_2[1], 'Name', curses.color_pair(color2))
    window.addstr(col_3[0], col_3[1], 'Parent\n', curses.color_pair(color2))

def pck_head(window, col_2, color1, color2, num):
    window.addstr('\nInterface', curses.color_pair(color1))
    window.addstr(col_2[0] + 1, col_2[1], 'PckSt / PckRecv\n', curses.color_pair(color2) | curses.A_BOLD)

def net_head(window, num1, num2):
    active_conn = num1 - num2
    window.addstr('\nNETWORK CONNECTIONS\n', curses.color_pair(4) | curses.A_BOLD)
    window.addstr('# active', curses.A_UNDERLINE)
    window.addstr(': ')
    window.addstr(str(active_conn) + '\n', curses.color_pair(7) | curses.A_BOLD)
    window.addstr('# closed', curses.A_UNDERLINE)
    window.addstr(': ')
    window.addstr(str(num2) + '\n', curses.color_pair(4) | curses.A_BOLD)

def usage(window, col):
    window.addstr(col[0], col[1] + 1,  'usage', curses.color_pair(3) | curses.A_BOLD | curses.A_UNDERLINE)
    window.addstr(':', curses.color_pair(3) | curses.A_BOLD)
    window.addstr(col[0] + 1, col[1], ' j,k,l,i,m', curses.color_pair(1) | curses.A_BOLD)
    window.addstr(' = ')
    window.addstr('procs', curses.color_pair(4) | curses.A_BOLD)
    window.addstr(col[0] + 2, col[1], ' b', curses.color_pair(1) | curses.A_BOLD)
    window.addstr(' = ')
    window.addstr('back', curses.color_pair(4) | curses.A_BOLD)
    window.addstr(col[0] + 3, col[1], ' a,s,d', curses.color_pair(1) | curses.A_BOLD)
    window.addstr(' = ')
    window.addstr('connects', curses.color_pair(4) | curses.A_BOLD)
    window.addstr(col[0] + 4, col[1], ' x', curses.color_pair(1) | curses.A_BOLD)
    window.addstr(' = ')
    window.addstr('back', curses.color_pair(4) | curses.A_BOLD)
    window.addstr(col[0] + 5, col[1] + 1, 'colours', curses.color_pair(1) | curses.A_UNDERLINE)
    window.addstr(':', curses.color_pair(1))
    window.addstr(col[0] + 6, col[1], ' red = ', curses.color_pair(2))
    window.addstr('root', curses.color_pair(2) | curses.A_BOLD)
    window.addstr(col[0] + 7, col[1], ' cyan = ', curses.color_pair(6))
    window.addstr('current usr', curses.color_pair(6) | curses.A_BOLD)
    window.addstr(col[0] + 8, col[1], ' yellow = ', curses.color_pair(5))
    window.addstr('other usr', curses.color_pair(5) | curses.A_BOLD)
    window.addstr(col[0] + 9, col[1], ' pink = ', curses.color_pair(7))
    window.addstr('OSX process', curses.color_pair(7) | curses.A_BOLD)
