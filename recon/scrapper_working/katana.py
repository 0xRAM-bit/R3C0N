import subprocess
import os
import threading
import time

mkdir = "crawled_subs"

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



class Katana:

    def __init__(self, filename):
        self.filename = filename

    def run_katana(self):
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

        cmd = f"katana -list {self.filename} -o crawled_subs/crawled.txt"

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
    import argparse

    parser = argparse.ArgumentParser(description='Run Katana for subdomain enumeration.')
    parser.add_argument('-f', '--file', required=True, help='File containing the list of subdomains')
    args = parser.parse_args()

    katana = Katana(args.file)
    result = spinner("Katana Subdomain Enumeration", "Running Katana", katana.run_katana)
    
    
    if result == 0:
        print("[✔] Katana completed successfully.")
    else:
        print("[✘] Katana failed to run.")