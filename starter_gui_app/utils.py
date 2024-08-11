
import termcolor
import traceback
import sys

# catches errors in gui and print them
def excepthook(etype, value, tb):
    if isinstance(value, KeyboardInterrupt):
        sys.exit(1)
    else:
        termcolor.cprint("Sorry, something's wrong! ", "yellow", file=sys.stderr)
        # print traceback
        traceback.print_exception(etype, value, tb)