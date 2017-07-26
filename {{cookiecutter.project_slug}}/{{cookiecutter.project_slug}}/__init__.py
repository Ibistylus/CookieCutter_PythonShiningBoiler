# -*- coding: utf-8 -*-

"""Top-level package for {{ cookiecutter.project_name }}."""
import logging

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = '{{ cookiecutter.email }}'
__version__ = '{{ cookiecutter.version }}'

logging.getLogger(__name__).addHandler(logging.NullHandler())
