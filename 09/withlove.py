from contextlib import contextmanager

import os

import paramiko

server = os.environ.get('192.168.178.**')
username = os.environ.get('**')
password = os.environ.get('**')

@contextmanager
def check_hostname(host):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username, password=password)
        yield ssh
    finally:
        ssh.close()


with check_hostname(server) as ssh:
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('cat /etc/hostname')
    print('%s' %ssh_stdout.readlines())