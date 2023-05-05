import paramiko

port = 22
host = "192.168.11.54"
username = "server"
password = "1qaz2wsx"
command = "python3 pelco-remoted/console.py -pr p -t com  -c right"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)
stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()
stdin.close()  # закрываем stdin
ssh.close()
print(lines)


