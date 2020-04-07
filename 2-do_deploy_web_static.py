#!/usr/bin/python3
"""Deploy an archive of static html to my web servers with Fabric3"""

from fabric import api
from fabric.contrib import files
import os


api.env.hosts = ['35.243.245.165', '54.243.21.33']
api.env.user = 'ubuntu'
api.env.key_filename = '~/.ssh/id_rsa'


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
