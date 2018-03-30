import logging

logger = logging.getLogger("{{cookiecutter.project_slug}}."+__name__)

def some_function():
    logger.info('a log entry created from a module and called some_function')