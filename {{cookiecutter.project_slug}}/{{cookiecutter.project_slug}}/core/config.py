#!/usr/bin/env python
import logging
import logging.config
import yaml
import sys
import os

logger = logging.getLogger("{{cookiecutter.project_slug}}."+__name__)
logging.basicConfig(level=logging.DEBUG)

user_path = os.path.realpath("/etc/")
user_project_path = os.path.realpath("/etc/{{cookiecutter.project_slug}}/")
cur_rel_path = os.path.relpath(os.path.join(os.path.dirname(__file__), "/../../etc/"))
cur_abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..\\", "..\\", "etc"))
env_var = os.environ.get("BOILERFIDDLER_CONF") or ""
settings = None
locations = [os.curdir, user_path, user_project_path, cur_rel_path, cur_abs_path, env_var]


def logging_configuration():

    config= None

    for loc in locations:
        path = (os.path.join(os.path.join(loc,"{{cookiecutter.project_slug}}.ini")))
        try:
            if os.path.isfile(path):
                logging.config.fileConfig(os.path.join(loc,"{{cookiecutter.project_slug}}.ini")) #, disable_existing_loggers=False
                logger.debug(str(os.path.exists(loc)) + " folder exists: " + str(os.path.isfile(path)) + " file exists: " + path )
        except IOError:
            logger.warning("A log ini file was not found")
            pass


def settings_configuration():

    for loc in locations:
        path = (os.path.join(os.path.join(loc, "{{cookiecutter.project_slug}}_settings.yaml")))

        try:
            if os.path.isfile(path):

                with open(path, "r") as f:

                    settings = yaml.load(f)
                    logger.debug(str(os.path.exists(loc)) + " folder exists: " + str(os.path.isfile(path)) + " file exists: " + path)

                    return settings
        except IOError as e:
            logger.warning("A log configuration was not found {}".format(e.args))
            raise e

logging_configuration()
settings = settings_configuration()

if settings is None:
    raise IOError("Settings.yaml was not found in the follow locations {}".format(locations))

logger.debug("Settings and logs configured")
