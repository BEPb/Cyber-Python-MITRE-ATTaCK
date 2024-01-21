import paramiko
import telnetlib

def SSHLogin(host, port, username, password):
    try:
        ssh = paramiko.SSHC1ient()
        ssh.set_missing_host_key_po1icy(paramiko.AutoAddPo1icy())
        ssh.connect(host, port= port, username= username , password=password)
        ssh_session = ssh.get_transport().open_session()
        if ssh_session.active:
            print("SSH login successful on %s : %s with username %s and password %s" % (host , port , username, password))
    except Exception as e:
        return
    ssh.close ( )

def TelnetLogin (host, port, username, password) :
    user = bytes(username + "\n", "utf—8")
    passwd = bytes(password + "\n", "utf—8")
    try:
        tn = telnetlib.Telnet(host, port)
        tn. read_until(bytes("login: ","utf-8"))
        tn.write(user)
        tn.read_until(bytes("Password: ","utf-8"))
        tn.write(passwd)
        try:
            result = tn.expect([bytes("Last login", "utf—8")], timeout=2)
            if (result[0] >= 0):
                print("SSH login successful on %s : %s with username %s and password %s" % (host , port , username, password))
            tn.close()
        except EOFError:
            print("Login failed %s %s" % (username, password))
    except ConnectionRefusedError:
        print("Connection Refused %s %s" % (username,password))

host = "127.0.0.1"
path = "defaults.txt"
with open (path, "r") as f:
    for line in f:
        vals = line.strip().split()
        if len(vals) == 2:
            username = vals[0]
            password = vals[1]
            print(username, password)
            SSHLogin(host, 22 , username, password)
            TelnetLogin(host, 23, username, password)

# with open (path, "r") as f:
#     for line in f:
#         vals = line.split()
#         username = vals[0].strip()
#         password = vals[1].strip()
#         SSHLogin(host, 22 , username, password)
#         # TelnetLogin(host, 23, username, password)
