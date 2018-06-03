###########################################################
###############       Colored Logger      #################
###########################################################

# Referecen: https://stackoverflow.com/questions/384076/how-can-i-color-python-logging-output
import logging 

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

#The background is set with 40 plus the number of the color, and the foreground with 30

#These are the sequences need to get colored ouput
RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[1;%dm"
BOLD_SEQ = "\033[1m"

def formatter_message(message, use_color = True):
    if use_color:
        message = message.replace("$RESET", RESET_SEQ).replace("$BOLD", BOLD_SEQ)
    else:
        message = message.replace("$RESET", "").replace("$BOLD", "")
    return message

COLORS = {
    'WARNING': YELLOW,
    'INFO': GREEN,
    'DEBUG': BLUE,
    'CRITICAL': YELLOW,
    'ERROR': RED
}

class ColoredFormatter(logging.Formatter):
    def __init__(self, msg, use_color = True):
        logging.Formatter.__init__(self, msg)
        self.use_color = use_color

    def format(self, record):
        name = record.name
        levelname = record.levelname
        if self.use_color and record.levelname in COLORS:
            name_color = COLOR_SEQ % (30 + COLORS[levelname]) + name + RESET_SEQ
            record.name = name_color
        return logging.Formatter.format(self, record)

# Custom logger class with multiple destinations
class ColoredLogger(logging.Logger):
    FORMAT = "[$BOLD%(name)-10s$RESET] %(message)s "
    # FORMAT = "[$BOLD%(name)-10s$RESET] %(message)s ($BOLD%(filename)s$RESET:%(lineno)d)"
    COLOR_FORMAT = formatter_message(FORMAT, True)
    def __init__(self, name=None, level="debug"):
        logging.Logger.__init__(self, name, logging.INFO if level=="info" else logging.DEBUG)                

        color_formatter = ColoredFormatter(self.COLOR_FORMAT)

        console = logging.StreamHandler()
        console.setFormatter(color_formatter)

        self.addHandler(console)
        return


logging.setLoggerClass(ColoredLogger)
logging.getLogger("PIL.PngImagePlugin").setLevel(logging.ERROR)

