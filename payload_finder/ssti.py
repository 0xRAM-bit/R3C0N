import json
import argparse

class SSTI:
    def __init__(self):
        pass
    def open_json_file(self, path):
        self.path = path
        with open(self.path, "r") as f:
            data = json.load(f)
            return data
    def show_payload_ssti_java(self):
        path = "ssti/java.json"
        payls = self.open_json_file(path)
        for p in payls["payloads"]:
            print(f"\033[92m[{p.get('type', '?')}] \033[94m[{p.get('tech', '?')}] \033[91m[{p.get('payload', '?')}]\033[0m")
    def show_payload_ssti_asp(self):
        path = "ssti/asp.json"
        payls = self.open_json_file(path)
        for p in payls["payloads"]:
            print(f"\033[92m[{p.get('type', '?')}]  \033[91m[{p.get('payload', '?')}]\033[0m")


