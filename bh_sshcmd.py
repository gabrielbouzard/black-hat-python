import threading
import paramiko
import subprocess

def ssh_command(ip, user, pkFileName, password, command):

    client = paramiko.SSHClient()
    client.load_system_host_keys('/home/gabriel/.ssh/known_hosts')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pk = paramiko.RSAKey.from_private_key_file(pkFileName, password)
    client.connect(ip, username=user, pkey=pk)
    ssh_session = client.get_transport().open_session()

    if ssh_session.active:
        ssh_session.exec_command(command)
        print(ssh_session.recv(1024))

    return

ssh_command('ipaddress', 'username', '/home/gabriel/.ssh/private_key', 'keyFile_password', 'id')
