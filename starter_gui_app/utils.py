import termcolor
import traceback
import sys
import os
import logging

__appname__ = "Starter"


def create_logger():
    app_path = os.path.dirname(__file__)
    app_log_path = os.path.join(app_path, "logs")

    if not os.path.exists(app_log_path):
        os.makedirs(app_log_path)

    log_file_name = __appname__ + ".txt"

    formatter = "%(asctime)s: %(name)s -%(levelname)s -%(module)s -%(funcName)s -%(lineno)-3d -%(message)s"
    logging.basicConfig(
        filename=os.path.join(app_log_path, log_file_name), format=formatter
    )
    logger = logging.getLogger(name="main-gui")
    logger.setLevel(logging.DEBUG)

    # Enable logging on the console
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter(formatter))
    ch.setLevel(logging.DEBUG)
    logger.addHandler(ch)


# catches errors in gui and print them
def excepthook(etype, value, tb):
    if isinstance(value, KeyboardInterrupt):
        sys.exit(1)
    else:
        termcolor.cprint("Sorry, something's wrong! ", "yellow", file=sys.stderr)
        # print traceback
        traceback.print_exception(etype, value, tb)
