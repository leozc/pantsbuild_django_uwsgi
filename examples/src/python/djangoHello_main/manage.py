#!/usr/bin/env python
import os
import sys


print (">> loaded script properly")
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoHello.settings")

    
    print (">> load Django in main {}".format(sys.argv))
    from django.core.management import execute_from_command_line

    print (">> load Django with sys arg {}".format(sys.argv))
    execute_from_command_line(sys.argv)
