# WannaKnow

## What Is It?

WannaKnow is a small dynamic network and process monitoring app written in Python.
It is mainly a wrapper built on top of the psutil library for data and the (n)curses
library for terminal rendering. The idea is to have a small tool which fetches data on
the various connections on the network, the user sessions, informs on processes in a dynamic
and easily readable way. This is something I created for myself so the information is formatted
in a way that suits my personal needs. I'm running on MacOsSierra so some of the information
is MacOs specific.

## What Did I Wanna Know?

Basically I was tired of trying to debug my network by running static commands in the cli like
netstat and so forth and dealing with the verbose output. These utilities are
amazing but not always easy for monitoring when you need to scroll through
hundreds of lines of input and run those
commands multiple times. I wanted something simple that could update in real time and tell me in a glance
what are the active connections, which processes are running, what are their pids and which process they
relate to without having all the verbose output.
The problem I found with other monitoring apps, although some of them are really good (LittleSnitch,
 HandsOff, and others), is that either they are not compatible with Sierra or they have an intrusive
behaviour and block processes from executing (which in many cases this is a good thing and blocking some
connections or process from executing is indeed what you want, only that was not the purpose I was looking
for).

## How?

WannaKnow is a wrapper around two really nice Python libraries:

### psutil

psutil (process and system utilities) is a cross-platform library for retrieving information on running
processes and system utilization (CPU, memory, disks, network, sensors) in Python. It is useful mainly for
system monitoring, profiling and limiting process resources and management of running processes. It
implements many functionalities offered by UNIX command line tools such as: ps, top, lsof, netstat,
ifconfig, who, df, kill, free, nice, ionice, iostat, iotop, uptime, pidof, tty, taskset, pmap.

This amazing library created by ''''' allows for the use of network utilities through python. Only issue,
some of these utilities need root permissions to run so in the case of WannaKnow, the app must be run with
superuser permissions (at least on recent versions of MacOs) in order to access the information.

To know more about the psutil library, you can refer to the documentation.

### (n)curses

Curses (or ncurses after some publishing issues) is a python library that allows for terminal manipulation.
On initialization, curses returns a window object the size of the current terminal in which it's possible to
draw and display information on.

For more information on curses, refer to the documentation.

## Usage

WannaKnow uses colour codes to try and make the information clearer to look at with a glance. On the left
side, information on the various sessions as well as packets coming in and out from the network is displayed
at the top, alongside a simple legend with basic usage and color explanation.

Below is the connections window, users can flip through rows of connections by using the keys 'a', 's', 'd'.
The 'x' character returns to display the first results.

On the right, all the processes are listed long with their pid number as well as the parent process name
and pid number. The parent processes are listed in white. The main processes are colour coded: red when a
process is ran as root, cyan (or light blue) when it is running as the current user and yellow for any
other user or permission. The pink colour is an exception, these are the apple specific processes (the
apple.com part of the name has been omitted for the sake of space) which I chose to give a different colour
so that I could keep track of them more clearly. In those cases, the name will appear in pink but the PID
will still be in the colour of the user in which the process is ran.

To keys 'j', 'k', 'l', 'i' and 'm' can be used to flip through different parts of the process listing. The
key 'b' will bring back to the top of the list.

## Issues

This is not a final prototype  and I'm far from being an experienced python programmer but on my machine it
runs well and basically does what I wanted it to do. For the app to work best, the terminal needs to be at
least 2/3 of the screen wide (in case of small screens). As mentioned before, because some of the psutil
functions used by the program require root permissions, WannaKnow needs to be run with sudo. I'm trying to
fix this so that the app can still run with less permissions and displays only the information that it can.
Their are also some crashing issues when the app runs for a while which I'm trying to solve.

## Next Steps

Their are a few fuctionalities I would like to try and implement, first I would like to try and make the
information relevant if the user is on Linux or Mac (adapt the specific MacOs process display).
Secondly, I would like to harness further the power of the psutil library by using it to display more
information windows that could be accessed on user input (basically adding more windows that the user could
flip through).

Twitter: @EarthAbigail
