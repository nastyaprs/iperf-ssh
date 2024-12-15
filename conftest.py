import paramiko
import subprocess
import pytest

server_ip = '192.168.0.73'
username = 'your_ssh_username'
password = 'your_ssh_password'

@pytest.fixture(scope='function')
def server():

    try:

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(server_ip, username=username, password=password)

        command = "iperf -s -D"
        ssh.exec_command(command)

        yield ssh

    finally:
        ssh.exec_command("killall iperf")
        ssh.close()


@pytest.fixture(scope='function')
def client(server):
    command = ["iperf", "-c", server_ip, "-t", "10", "-f", "m"]
    result = subprocess.run(command, capture_output=True, text=True)
    return result
