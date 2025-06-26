#!/usr/bin/python3
""" generates tgz files """
from fabric.api import local
from datetime import datetime


def do_pack():
    """ generates .tgz """
    date = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    local(" mkdir -p versions")
    file = "versions/web_static_{}.tgz".format(date)
    local("sudo tar -cvzf versions/web_static_{}.tgz web_static/".format(date))
    return file
