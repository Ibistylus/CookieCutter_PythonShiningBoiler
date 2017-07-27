# -*- coding: utf-8 -*-

"""Main module."""

from core.config import settings
from core.config import logger

import {{cookiecutter.project_slug}}_a_module

def sample_function():
    logger.info("sample_function ran")

def main():
    logger.debug("Prior to configuration")
    sample_function()
    {{cookiecutter.project_slug}}_a_module.some_function()
    
if __name__ == '__main__':  
    main()