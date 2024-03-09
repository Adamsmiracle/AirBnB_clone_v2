#!/usr/bin/python3
# Generates a .tgz archive from the contents of web_static.
import os.path
from fabric.api import local
from datetime import datetime


def do_pack():
    """Create a tar gzipped archive"""
    date = datetime.utcnow()
    file_name = "web_static_{}{}{}{}{}{}.tgz"
    dates = "date.year, date.month, date.day,date.hour,date.minute,date.second"
    file = f"versions/{file_name}".format()
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
