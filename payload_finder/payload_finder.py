import json
import os

_BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class SSTI:
    def __init__(self):
        pass
    def _open_json_file(self, path):
        with open(path, "r") as f:
            return json.load(f)

    def show_payload(self, tech):
        tech_map = {
            "java": "ssti/java.json",
            "asp": "ssti/asp.json",
            "javascript": "ssti/javascript.json",
            "php": "ssti/php.json",
            "python": "ssti/python.json"
        }
        if tech not in tech_map:
            print("please specify the right technology for SSTI: asp, java")
            return
        
        path = os.path.join(_BASE_DIR, tech_map[tech])
        try:
            payls = self._open_json_file(path)
            for p in payls["payloads"]:
                if tech == 'java' or tech == 'javascript' or tech == "php" or tech == "python":
                    print(f"\033[92m[{p.get('type', '?')}] \033[94m[{p.get('tech', '?')}] \033[91m[{p.get('payload', '?')}]\033[0m")
                else: 
                    print(f"\033[92m[{p.get('type', '?')}]  \033[91m[{p.get('payload', '?')}]\033[0m")
        except FileNotFoundError:
            print(f"Payload file not found: {path}")

class XSS:
    def __init__(self):
        pass

    def _open_json(self, path):
        with open(path, 'r') as f:
            return json.load(f)

    def show_payload(self, tech):
        tech_map = {
            "filter_bypass": "xss/filter_bypass.json",
            "polyglot": "xss/polyglot_xss.json",
            "WAF_bypass": "xss/waf_bypass.json",
            "csp_bypass": "xss/csp_bypass.json",
            "generic": "xss/generic.json"
        }

        if tech not in tech_map:
            print(f"Please specify the right technology for XSS.")
            return
        
        path = os.path.join(_BASE_DIR, tech_map[tech])
        try:
            data = self._open_json(path)
            for p in data.get("payloads", []):
                print(f"\033[92m[{p.get('type', '?')}] \033[91m[{p.get('payload', '?')}]\033[0m")
        except FileNotFoundError:
            print(f"Payload file not found: {path}")

class SQLI:
    def __init__(self):
        pass

    def _open_json(self, path):
        with open(path, 'r') as f:
            return json.load(f)

    def _open_txt(self, path):
        with open(path, 'r') as f:
            return f.readlines()

    def show_payload(self, tech):
        json_tech_map = {
            "mysql": "sqli/mysql.json",
            "postgres": "sqli/postgres.json",
            "generic": "sqli/generic.json"
        }
        txt_tech_map = {
            "auth_bypass": "sqli/auth_bypass.txt",
            "time_based": "sqli/time_based.txt",
            "polyglot": "sqli/SQLi_Polyglots.txt"
        }

        if tech in json_tech_map:
            path = os.path.join(_BASE_DIR, json_tech_map[tech])
            try:
                data = self._open_json(path)
                for p in data.get("payloads", []):
                    print(f"\033[92m[{p.get('type', '?')}] \033[91m[{p.get('payload', '?')}]\033[0m")
            except FileNotFoundError:
                print(f"Payload file not found: {path}")

        elif tech in txt_tech_map:
            path = os.path.join(_BASE_DIR, txt_tech_map[tech])
            try:
                lines = self._open_txt(path)
                for line in lines:
                    payload = line.strip()
                    if payload:
                        print(f"\033[92m[{tech}] \033[91m[{payload}]\033[0m")
            except FileNotFoundError:
                print(f"Payload file not found: {path}")
        else:
            print(f"Please specify the right technology for SQLi.")

class Bypass_403_401():
    def __init__(self):
        pass
    def _open_json(self, path):
        with open(path, 'r') as f:
            return json.load(f)
    def show_payload(self):
        tech_map = {
            "403_bypass": "403_401_bypass/403_401.json"
        }
        tech = "403_bypass"
        if tech not in tech_map:
            print("please specify the right technology")
            return
        
        path = os.path.join(_BASE_DIR, tech_map[tech])
        try:
            payls = self._open_json(path)
            for p in payls["payloads"]:
                if tech == "403_bypass":
                    print(f"\033[92m[{p.get('type', '?')}] \033[94m[{p.get('tech', '?')}] \033[91m[{p.get('payload', '?')}]\033[0m")
                else: 
                    print("Not found")
        except FileNotFoundError:
            print(f"Payload file not found: {path}")

class CRLF_INJECTION():
    def __init__(self):
        pass

    def _open_txt(self, path):
        with open(path, 'r') as f:
            return f.readlines()
        
    def show_payload(self):
        path = os.path.join(_BASE_DIR, "crlf/crlf.txt")
        lines = self._open_txt(path)
        for line in lines:
            payload = line.strip()
            if payload:
                print(f"\033[92m[CRLF] \033[91m[{payload}]\033[0m")
            else:
                print("Not found")
# a = Bypass_403_401()
# a.show_payload()