import subprocess
import threading
import time
import argparse
import os




def spinner(task_name, message, target_func, *args, **kwargs):
    spinner_chars = ['|', '/', '-', '\\']
    idx = 0
    stop_flag = False
    result = {"code": 1}  

    def spin():
        nonlocal idx
        while not stop_flag:
            print(f"\r[{spinner_chars[idx % len(spinner_chars)]}] {message} ", end='', flush=True)
            idx += 1
            time.sleep(0.1)

    
    thread = threading.Thread(target=spin)
    thread.start()

    try:
        code = target_func(*args, **kwargs)
        result["code"] = code
    finally:
        stop_flag = True
        thread.join()
        if result["code"] == 0:
            print(f"\r[✔] Done: {task_name}                ")
        else:
            print(f"\r[✘] Failed: {task_name}              ")

    return result["code"]



class Adv_Subs:


    def __init__(self, domain, api):
        self.domain = domain
        self.api = api

    def run_adv_subs(self):
        mkdir = f"{self.domain}_subs"
        try:
            os.mkdir(mkdir)
        except FileExistsError:
            pass
        except PermissionError:
            print("Permission denied: Unable to create directory for crawled subtitles.")
            exit(1)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            exit(1)
        
        cmd = f"chaos-client -d {self.domain} -key {self.api} | httpx -silent -o {self.domain}_subs/adv_subs.txt"
        try:
            subprocess.run(cmd, check=True, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return 0
        except subprocess.CalledProcessError as e:
            return 1
        except FileNotFoundError:
            print("\n[!] ADV not found. Please install it.")
            return 1
        except Exception as e:
            print(f"\n[!] Unexpected error in ADV: {e}")
            return 1
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run advanced subdomain enumeration.')
    parser.add_argument('-d', '--domain', required=True, help='Target domain to enumerate subdomains')
    parser.add_argument('-a', '--api', required=True, help='API key for chaos-client visit https://cloud.projectdiscovery.io')

    args = parser.parse_args()

    adv_subs = Adv_Subs(args.domain, args.api)
    result = spinner("Advanced Subdomain Enumeration", "Running advanced subdomain enumeration...", adv_subs.run_adv_subs)

    if result == 0:
        print("[+] Advanced subdomain enumeration completed successfully.")
    else:
        print("[x] Advanced subdomain enumeration encountered an error.")
