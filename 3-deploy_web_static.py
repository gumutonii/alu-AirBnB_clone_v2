#!/usr/bin/python3
<<<<<<< HEAD
"""
    Fabric script that creates and distributes an archive to the web servers.
"""
from os import makedirs, path
from datetime import datetime
from fabric.api import env, local, put, run

env.hosts = ['35.229.40.200', '35.229.23.118']


def do_pack():
    """ Function that generates the archive. """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(timestamp)

    try:
        makedirs("./versions", exist_ok=True)
        local('tar -cvzf {} web_static'.format(file_path))
        return file_path

    except:
        return None


def do_deploy(archive_path):
    """ Function that distributes the archive.

    Args:
        archive_path (str): the path of the archive to deploy on the servers.
    """

    try:
        if not path.exists(archive_path):
            raise FileNotFoundError

        name = archive_path.split("/")[-1]
        name_no_ext = name.split(".")[0]

        remote = "/data/web_static/releases"
        dest = "{}/{}".format(remote, name_no_ext)

        put(archive_path, '/tmp')
        run('mkdir -p {}/'.format(dest))
        run('tar -xzf /tmp/{} -C {}'.format(name, dest))
        run('rm /tmp/{}'.format(name))
        run('mv {}/web_static/* {}/'.format(dest, dest))
        run('rm -rf {}/web_static'.format(dest))
        run('rm -rf /data/web_static/current')
        run('ln -s {}/ /data/web_static/current'.format(dest))

    except:
        print("Error. Version deploy aborted")
        return False

    print("New version deployed!")
=======
# Fabfile to create and distribute an archive to a web server.
import os.path
from datetime import datetime
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run

env.hosts = ["54.174.230.101", "100.26.57.164"]


def do_pack():
    """ create a tar gzipped archive of the directory web_static """
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file


def do_deploy(archive_path):
    """
        Function to distribute archive to a web server
        Args:
        archive_path (str): path to the archive to be distributed
        Return:
        False - if the file at the path archive_path doesn't exist
        True - otherwise
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
>>>>>>> 070b2400c65851cfed794515179027bbfa97752b
    return True


def deploy():
<<<<<<< HEAD
    """ Function that generates and distributes the archive. """
    if archive_to_deploy:
        return do_deploy(archive_to_deploy)
    else:
        return False

archive_to_deploy = do_pack()
=======
    """ create & distribute an archive to a web server """
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
>>>>>>> 070b2400c65851cfed794515179027bbfa97752b
