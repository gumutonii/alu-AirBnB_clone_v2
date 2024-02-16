#!/usr/bin/python3
"""Fabric script to distribute an archive to web servers."""
from fabric.api import *
from os import path

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'  # or whatever username you use
env.key_filename = ['my_ssh_private_key']


def do_deploy(archive_path):
    """Distribute an archive to web servers."""
    if not path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        file_name = archive_path.split('/')[-1]
        folder_name = file_name.split('.')[0]

        run('mkdir -p /data/web_static/releases/{}/'.format(folder_name))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(file_name, folder_name))
        run('rm /tmp/{}'.format(file_name))
        run('mv /data/web_static/releases/{}/web_static/* '
            '/data/web_static/releases/{}/'.format(folder_name, folder_name))
        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(folder_name))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ '
            '/data/web_static/current'.format(folder_name))
        print("New version deployed!")
        return True
    except:
        return False


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    from datetime import datetime
    dt = datetime.utcnow()
    file_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                             dt.month,
                                                             dt.day,
                                                             dt.hour,
                                                             dt.minute,
                                                             dt.second)
    # Create the 'versions' directory if it doesn't exist
    if not path.isdir("versions"):
        local("mkdir -p versions")

    # Create the .tgz archive
    if local("tar -cvzf {} web_static".format(file_name)).failed:
        return None

    return file_name
