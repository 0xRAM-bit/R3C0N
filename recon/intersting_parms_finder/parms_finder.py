import argparse
import os
import re



# import subprocess
# import os
# import threading
# import time
# import argparse
# import re

# mkdir = "parms_fuzzer"

xss_parms = [
    "q=",
    "s=",
    "search=",
    "lang=",
    "keyword=",
    "query=",
    "page=",
    "keywords=",
    "year=",
    "view=",
    "email=",
    "type=",
    "name=",
    "p=",
    "callback=",
    "jsonp=",
    "api_key=",
    "api=",
    "password=",
    "email=",
    "emailto=",
    "token=",
    "username=",
    "csrf_token=",
    "unsubscribe_token=",
    "id=",
    "item=",
    "page_id=",
    "month=",
    "immagine=",
    "list_type=",
    "url=",
    "terms=",
    "categoryid=",
    "key=",
    "l=",
    "begindate=",
    "enddate="
]

sql_parms = [
    "id=",
    "select=",
    "report=",
    "role=",
    "update=",
    "query=",
    "user=",
    "name=",
    "sort=",
    "where=",
    "search=",
    "params=",
    "process=",
    "row=",
    "view=",
    "table=",
    "from=",
    "sel=",
    "results=",
    "sleep=",
    "fetch=",
    "order=",
    "keyword=",
    "column=",
    "field=",
    "delete=",
    "string=",
    "number=",
    "filter="
]

ssti_parms = [
    "template=",
    "preview=",
    "id=",
    "view=",
    "activity=",
    "name=",
    "content=",
    "redirect="
]

rce_parms = [
    "daemon=",
    "upload=",
    "dir=",
    "download=",
    "log=",
    "ip=",
    "cli=",
    "cmd=",
    "exec=",
    "command=",
    "execute=",
    "ping=",
    "query=",
    "jump=",
    "code=",
    "reg=",
    "do=",
    "func=",
    "arg=",
    "option=",
    "load=",
    "process=",
    "step=",
    "read=",
    "function",
    "req=",
    "feature=",
    "exe=",
    "module=",
    "payload=",
    "run=",
    "print="
]


lfi_parms = [
    "file=",
    "document=",
    "folder=",
    "root=",
    "path=",
    "pg=",
    "style=",
    "pdf=",
    "template=",
    "php_path=",
    "doc=",
    "page=",
    "name=",
    "cat=",
    "dir=",
    "action=",
    "board=",
    "date=",
    "detail=",
    "download=",
    "prefix=",
    "include=",
    "inc=",
    "locate=",
    "show=",
    "site=",
    "type=",
    "view=",
    "content=",
    "layout=",
    "mod=",
    "conf=",
    "url="
]


idor_parms = [
    "id=",
    "user=",
    "account=",
    "number=",
    "order=",
    "no=",
    "doc=",
    "key=",
    "email=",
    "group=",
    "profile=",
    "edit=",
    "report="
]

intersting_parms = [
    "template=",
    "preview=",
    "id=",
    "view=",
    "activity=",
    "name=",
    "content=",
    "redirect=",
    "(&|[?])access(&|=)",
    "(&|[?])admin(&|=)",
    "(&|[?])dbg(&|=)",
    "(&|[?])debug(&|=)",
    "(&|[?])edit(&|=)",
    "(&|[?])grant(&|=)",
    "(&|[?])test(&|=)",
    "(&|[?])alter(&|=)",
    "(&|[?])clone(&|=)",
    "(&|[?])create(&|=)",
    "(&|[?])delete(&|=)",
    "(&|[?])disable(&|=)",
    "(&|[?])enable(&|=)",
    "(&|[?])exec(&|=)",
    "(&|[?])execute(&|=)",
    "(&|[?])load(&|=)",
    "(&|[?])make(&|=)",
    "(&|[?])modify(&|=)",
    "(&|[?])rename(&|=)",
    "(&|[?])reset(&|=)",
    "(&|[?])shell(&|=)",
    "(&|[?])toggle(&|=)",
    "(&|[?])adm(&|=)",
    "(&|[?])root(&|=)",
    "(&|[?])cfg(&|=)",
    "(&|[?])dest(&|=)",
    "(&|[?])redirect(&|=)",
    "(&|[?])uri(&|=)",
    "(&|[?])path(&|=)",
    "(&|[?])continue(&|=)",
    "(&|[?])url(&|=)",
    "(&|[?])window(&|=)",
    "(&|[?])next(&|=)",
    "(&|[?])data(&|=)",
    "(&|[?])reference(&|=)",
    "(&|[?])site(&|=)",
    "(&|[?])html(&|=)",
    "(&|[?])val(&|=)",
    "(&|[?])validate(&|=)",
    "(&|[?])domain(&|=)",
    "(&|[?])callback(&|=)",
    "(&|[?])return(&|=)",
    "(&|[?])feed(&|=)",
    "(&|[?])host(&|=)",
    "(&|[?])port(&|=)",
    "(&|[?])to(&|=)",
    "(&|[?])out(&|=)",
    "(&|[?])view(&|=)",
    "(&|[?])dir(&|=)",
    "(&|[?])show(&|=)",
    "(&|[?])navigation(&|=)",
    "(&|[?])open(&|=)",
    "(&|[?])file(&|=)",
    "(&|[?])document(&|=)",
    "(&|[?])folder(&|=)",
    "(&|[?])pg(&|=)",
    "(&|[?])php_path(&|=)",
    "(&|[?])style(&|=)",
    "(&|[?])doc(&|=)",
    "(&|[?])img(&|=)",
    "(&|[?])filename(&|=)",
    "id=",
    "select=",
    "report=",
    "role=",
    "update=",
    "query=",
    "user=",
    "name=",
    "sort=",
    "where=",
    "search=",
    "params=",
    "process=",
    "row=",
    "view=",
    "table=",
    "from=",
    "sel=",
    "results=",
    "sleep=",
    "fetch=",
    "order=",
    "keyword=",
    "column=",
    "field=",
    "delete=",
    "string=",
    "number=",
    "filter=",
    "(&|[?])callback=",
    "(&|[?])cgi-bin/redirect.cgi",
    "(&|[?])checkout=",
    "(&|[?])checkout_url=",
    "(&|[?])continue=",
    "(&|[?])data=",
    "(&|[?])dest=",
    "(&|[?])destination=",
    "(&|[?])dir=",
    "(&|[?])domain=",
    "(&|[?])feed=",
    "(&|[?])file=",
    "(&|[?])file_name=",
    "(&|[?])file_url=",
    "(&|[?])folder=",
    "(&|[?])folder_url=",
    "(&|[?])forward=",
    "(&|[?])from_url=",
    "(&|[?])go=",
    "(&|[?])goto=",
    "(&|[?])host=",
    "(&|[?])html=",
    "(&|[?])image_url=",
    "(&|[?])img_url=",
    "(&|[?])load_file=",
    "(&|[?])load_url=",
    "(&|[?])login_url=",
    "(&|[?])logout=",
    "(&|[?])navigation=",
    "(&|[?])next=",
    "(&|[?])next_page=",
    "(&|[?])Open=",
    "(&|[?])out=",
    "(&|[?])page_url=",
    "(&|[?])path=",
    "(&|[?])port=",
    "(&|[?])redir=",
    "(&|[?])redirect=",
    "(&|[?])redirect_to=",
    "(&|[?])redirect_uri=",
    "(&|[?])redirect_url=",
    "(&|[?])reference=",
    "(&|[?])return=",
    "(&|[?])return_path=",
    "(&|[?])return_to=",
    "(&|[?])returnTo=",
    "(&|[?])return_url=",
    "(&|[?])rt=",
    "(&|[?])rurl=",
    "(&|[?])show=",
    "(&|[?])site=",
    "(&|[?])target=",
    "(&|[?])to=",
    "(&|[?])uri=",
    "(&|[?])url=",
    "(&|[?])val=",
    "(&|[?])validate=",
    "(&|[?])view=",
    "(&|[?])window=",
    "daemon=",
    "upload=",
    "dir=",
    "execute=",
    "download=",
    "log=",
    "ip=",
    "cli=",
    "cmd=",
    "file=",
    "document=",
    "folder=",
    "root=",
    "path=",
    "pg=",
    "style=",
    "pdf=",
    "template=",
    "php_path=",
    "doc=",
    "page=",
    "name=",
    "id=",
    "user=",
    "account=",
    "number=",
    "order=",
    "no=",
    "doc=",
    "key=",
    "email=",
    "group=",
    "profile=",
    "edit=",
    "report=",
    "access=",
    "admin=",
    "dbg=",
    "debug=",
    "edit=",
    "grant=",
    "test=",
    "alter=",
    "clone=",
    "create=",
    "delete=",
    "disable=",
    "enable=",
    "exec=",
    "execute=",
    "load=",
    "make=",
    "modify=",
    "rename=",
    "reset=",
    "shell=",
    "toggle=",
    "adm=",
    "root=",
    "cfg=",
    "config="
]

js_parms = [
    ".js"
]

class ParmsFinder:
    
    
    def __init__(self, param, file):
        self.param = param
        self.file = file

    def find_parms(self):
        mkdir = f"{self.param}_parameters"
        try:
            os.mkdir(mkdir)
        except FileExistsError:
            pass
        except PermissionError:
            print(f"Permission denied: Unable to create directory '{mkdir}'.")
            exit(1)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            exit(1)

        
        param_map = {
            'xss': xss_parms,
            'sql': sql_parms,
            'ssti': ssti_parms,
            'rce': rce_parms,
            'lfi': lfi_parms,
            'idor': idor_parms,
            'interesting': intersting_parms,
            'js': js_parms
        }

        if self.param not in param_map:
            print(f"Error: Unknown param type '{self.param}'. Available: {', '.join(param_map.keys())}")
            return 1

        selected_parms = param_map[self.param]
        output_file = os.path.join(mkdir, f"{self.param}_parms.txt")

        try:
            with open(self.file, 'r') as f_in, open(output_file, 'w') as f_out:
                for line in f_in:
                    for parm in selected_parms:
                        
                        if parm.startswith('(&|[?])') or parm.endswith('='):
                            try:
                                if re.search(parm, line):
                                    f_out.write(line)
                                    break
                            except re.error:
                                if parm in line:
                                    f_out.write(line)
                                    break
                        else:
                            if parm in line:
                                f_out.write(line)
                                break
            return 0
        except FileNotFoundError:
            print(f"Error: Input file '{self.file}' not found.")
            return 1
        except Exception as e:
            print(f"An error occurred while processing the file: {e}")
            return 1

if __name__ == "__main__":
    available_parms = ['xss', 'sql', 'ssti', 'rce', 'lfi', 'idor', 'interesting', 'js']
    parser = argparse.ArgumentParser(
        description='Find URLs with specific parameters.'
    )
    parser.add_argument(
        '-p', '--param', required=True,
        help=f"Parameter set to search for. Available: [----->] {', '.join(available_parms)}"
    )
    parser.add_argument(
        '-f', '--file', required=True,
        help='File containing URLs to search (e.g., "katana.txt")'
    )

    args = parser.parse_args()

    finder = ParmsFinder(args.param, args.file)
    result = finder.find_parms()

    if result == 0:
        print(f"[+] Successfully found parameters and saved to '{args.param}_parms.txt'")
    else:
        print("[x] An error occurred during parameter finding.")
