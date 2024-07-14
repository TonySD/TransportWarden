import logging
import colorama
import sys
from config import LOG_LEVEL, LOG_FILENAME

colorama.init()
logging.basicConfig(level=LOG_LEVEL)

class CustomFormatter(logging.Formatter):
    prefix = "[%(levelname)s : %(name)s]"
    format = " %(asctime)s - %(message)s"

    FORMATS = {
        logging.DEBUG: colorama.Fore.CYAN + prefix + colorama.Style.RESET_ALL + format,
        logging.INFO: colorama.Fore.BLUE + prefix + colorama.Style.RESET_ALL + format,
        logging.WARNING: colorama.Fore.YELLOW + prefix + colorama.Style.RESET_ALL + format,
        logging.ERROR: colorama.Fore.RED + prefix + colorama.Style.RESET_ALL + format,
        logging.CRITICAL: colorama.Back.RED + prefix + colorama.Style.RESET_ALL + format
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def get_logger(name: str = "root") -> logging.Logger:
    log = logging.getLogger(name)
    log.propagate = False

    stdout = logging.StreamHandler(stream=sys.stdout)
    stdout.setFormatter(CustomFormatter())
    log.addHandler(stdout)

    if LOG_FILENAME != None:
        file = logging.FileHandler(LOG_FILENAME)
        log.addHandler(file)

    return log
