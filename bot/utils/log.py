import logging


def _info_filter(record: logging.LogRecord) -> bool:
    return 20 <= record.levelno < 30


def _warn_filter(record: logging.LogRecord) -> bool:
    return 30 <= record.levelno


def get_logging_handlers() -> tuple:
    console = logging.StreamHandler()
    info = logging.FileHandler("info.log")
    info.addFilter(_info_filter)

    warn = logging.FileHandler("warn.log")
    warn.setLevel(logging.WARNING)
    warn.addFilter(_warn_filter)

    return console, info, warn
