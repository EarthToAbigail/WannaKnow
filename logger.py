import logging, sys, os

# #Set up a stream logger that outputs to console only when important errors arrise
# console = logging.StreamHandler(stream=sys.stdout)
# console.setLevel(logging.ERROR)
# #Set up formatters
# cslFormat = logging.Formatter('%(name)-8s : %(levelname)-8s : %(message)s')
# console.setFormatter(cslFormat)
# #Set root logger
# root = logging.getLogger()
# root.addHandler(console)

#Set up file logger to log verbose output and timestamps
def logToFile(filename, logger, message):
    #Set up a file handler
    logging.basicConfig(filename=filename,
                        filemode='w',
                        level=logging.DEBUG,
                        format='%(asctime)s :: %(name)-8s :: %(levelname)-8s :: %(message)s')
    try:
        logger.info(message)
    except Error:
        print('Could not log to file!')

monitor = logging.getLogger('monitor')
main = logging.getLogger('main')
