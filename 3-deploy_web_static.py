#!/usr/bin/python3
"""Tar, transfer, and deploy static html to webservers"""

from fabric import api, decorators
from fabric.contrib import files
from datetime import datetime
import os

api.env.hosts = ['142.44.167.235', '144.217.246.199']
api.env.user = 'ubuntu'
api.env.key_filename = '~/.ssh/id_rsa'


def deploy():
    """Wrapper function to pack html files into tarl and transfer
    to web servers."""
    return do_deploy(do_pack())


@decorators.runs_once
def do_pack():
    """create tar of webstatic files from the web_static
    folder
    """
    with api.settings(warn_only=True):
        isdir = os.path.isdir('versions')
        if not isdir:
            mkdir = api.local('mkdir versions')
            if mkdir.failed:
                return None
            suffix = datetime.now().strftime('%Y%m%d%M%S')
            path = 'versions/web_static_{}.tgz'.format(suffix)
            tar = api.local('tar -cvzf {} web_static'.format(path))
            if tar.failed:
                return None
            size = os.stat(path).st_size
            print('web_static packed: {} -> {}Bytes'.format(path, size))
            return path

def do_deploy(archive_path):
    """
    transfer `archive_path` to web servers.
    """
    if not os.path.isfile(archive_path):
        return False
    with api.cd('/tmp'):
        basename = os.path.basename(archive_path)
        fname, ext = os.path.splitext(basename)
        output_path = '/data/web_static/releases/{}'.format(fname)
        try:
            ppath = api.put(archive_path)
            if files.exists(output_path):
                api.run('rm -rdf {}'.format(output_path))
                api.run('mkdir -p {}/'.format(output_path))
                api.run('tar -xzf {} -C {}/'.format(ppath[0], output_path))
                api.run('rm -f {}'.format(ppath[0]))
                api.run('mv -u {}/web_static/* {}/'.format(
                    output_path, output_path))
                api.run('rm -rf {}/web_static'.format(output_path))
                api.run('rm -rf /data/web_static/current')
                api.run('ln -sf {}/ /data/web_static/current'.format(output_path))
                print('New version deployed!')
        except:
                        return False
        else:
                        return True
