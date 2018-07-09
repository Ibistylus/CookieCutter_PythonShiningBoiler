# -*- coding: utf-8 -*-

"""Main module."""
import logging
from {{cookiecutter.project_slug}}.core.config import settings
from {{cookiecutter.project_slug}}.core.config import logger

import {{cookiecutter.project_slug}}.{{cookiecutter.project_slug}}_a_module

logger = logging.getLogger("{{cookiecutter.project_slug}}."+__name__)


def sample_function():
    logger.info("sample_function ran")


def main():
    logger.debug("Prior to configuration")
    sample_function()
    {{cookiecutter.project_slug}}_a_module.some_function()


if __name__ == '__main__':
    main()
