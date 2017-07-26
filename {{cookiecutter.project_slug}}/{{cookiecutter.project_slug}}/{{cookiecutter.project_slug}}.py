# -*- coding: utf-8 -*-

"""Main module."""

import logging
import logging.config
import sys
import os

import {{cookiecutter.project_slug}}_a_module

 
logger = logging.getLogger("{{cookiecutter.project_slug}}")
logging.basicConfig(level=logging.DEBUG)

def sample_function():
    logger.info("sample_function ran")

def logging_configuration():
    
    config= None
    
    env_var = os.environ.get("{{cookiecutter.project_slug.upper()}}_CONF") or ""  
    cur_abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__),''))
    user_path = os.path.realpath("/etc/")
    user_project_path = os.path.realpath("/etc/{{cookiecutter.project_slug}}/")
    cur_rel_path = os.path.relpath(os.path.join(os.path.dirname(__file__),"../etc/")) 
    
    locations = [os.curdir,  user_path, user_project_path, cur_rel_path, cur_abs_path, env_var] 
    
    for loc in locations:
        path = (os.path.join(os.path.join(loc,"{{cookiecutter.project_slug}}.ini")))
        try: 
            if os.path.isfile(path): 
                logging.config.fileConfig(os.path.join(loc,"{{cookiecutter.project_slug}}.ini"), disable_existing_loggers=False)
                logger.debug(str(os.path.exists(loc)) + " folder exists: " + str(os.path.isfile(path)) + " file exists: " + path )
                     
        except IOError:
            logger.warning("A log ini file was not found")
            pass


def main():
    logger.debug("Prior to configuration")
    logging_configuration()
    logger.debug("will this print?")
    logger.debug("main ran")
    sample_function()
    {{cookiecutter.project_slug}}_a_module.some_function()
    
if __name__ == '__main__':  
    main()