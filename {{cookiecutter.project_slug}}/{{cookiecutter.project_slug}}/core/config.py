#!/usr/bin/env python
import logging
import logging.config
import yaml
import sys
import os

logger = logging.getLogger("{{cookiecutter.project_slug}}."+__name__)
logging.basicConfig(level=logging.DEBUG)

# Check environment variables first:
env_var = os.environ.get("{{cookiecutter.project_slug}}") or ""


# Check home directory second:
user_path = os.path.normpath(os.path.join(os.path.expanduser('~'), ".config/{{cookiecutter.project_slug}}"))


# Check project path last: 
user_project_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../etc")

settings = None
locations = [env_var, os.curdir, user_path, user_project_path]


def logging_configuration():

    config= None

    for loc in locations:
        path = os.path.normpath(os.path.join(os.path.join(loc,"{{cookiecutter.project_slug}}.ini")))
        try:
            if os.path.isfile(path):
                logging.config.fileConfig(path)
                break
        except Exception as e:
            logger.warning("Log ini file was not found")
            pass 

    if logging.config is None:
        logging.basicConfig(level=logging.WARNING)
        logger.warning("Log ini file was not found")
    else:
        logger.debug("Logging configuration was set. Log level: {}, loggers:{}".format(logger.level, logger.name))

def settings_configuration():

    for loc in locations:
        path = os.path.normpath(os.path.join(os.path.join(loc, "{{cookiecutter.project_slug}}_settings.yaml")))

        try:
            if os.path.isfile(path):
                with open(path, "r") as f:
                    settings = yaml.load(f)
                    return settings
        except IOError as e:
            logger.warning("A log configuration was not found {}".format(e.args))
            raise  e

logging_configuration()
settings = settings_configuration()

if settings is None:
    raise IOError("Settings.yaml was not found in the follow locations {}".format(locations))

logger.debug("Settings and logs configured")
