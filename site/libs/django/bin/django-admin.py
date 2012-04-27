#!/usr/bin/env python
import sys
sys.path += ['./libs/']

from django.core import management

if __name__ == "__main__":
    management.execute_from_command_line()
