import subprocess
import threading
import time
import argparse
from Normal_recon.sorting import Sorting

# Spinner function
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


class SubdomainENUM:
    def __init__(self, url):
        self.url = url

    # def run_amass(self):
    #     cmd = ['amass', 'enum', '-passive', '-d', f'{self.url}', '-o', 'amass_output.txt']
    #     try:
    #         subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    #         return 0
    #     except subprocess.CalledProcessError as e:
    #         return 1
    #     except FileNotFoundError:
    #         print("\n[!] Amass not found. Please install it.")
    #         return 1
    #     except Exception as e:
    #         print(f"\n[!] Unexpected error in Amass: {e}")
    #         return 1

    def run_subfinder(self):
        cmd = ['subfinder', '-d', f'{self.url}', '-all', '-o', 'subfinder.txt']
        try:
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return 0
        except subprocess.CalledProcessError as e:
            return 1
        except FileNotFoundError:
            print("\n[!] Subfinder not found. Please install it.")
            return 1
        except Exception as e:
            print(f"\n[!] Unexpected error in Subfinder: {e}")
            return 1

    def run_assetfinder(self):
        cmd = ['assetfinder', '-subs-only', f'{self.url}']
        try:
            with open("asset.txt", "a") as f:
                subprocess.run(cmd, check=True, stdout=f, stderr=subprocess.DEVNULL)
            return 0
        except subprocess.CalledProcessError as e:
            return 1
        except FileNotFoundError:
            print("\n[!] Assetfinder not found. Please install it.")
            return 1
        except Exception as e:
            print(f"\n[!] Unexpected error in Assetfinder: {e}")
            return 1



def run_subdomain_enum(url): # Initialzing the tools here
    subdomain_enum = SubdomainENUM(url)

    print("[+] Starting subdomain enumeration...\n")

    # if spinner("amass", f"Running amass on {url}", subdomain_enum.run_amass) != 0:
    #     return 1
    if spinner("subfinder", f"Running subfinder on {url}", subdomain_enum.run_subfinder) != 0:
        return 1
    if spinner("assetfinder", f"Running assetfinder on {url}", subdomain_enum.run_assetfinder) != 0:
        return 1

    print("\n[+] Subdomain enumeration completed successfully")
    return 0

def sort_subdomains():
    sorting = Sorting("subfinder.txt", "asset.txt")
    print("[+] Sorting subdomains...\n")

    if spinner("Sorting", "Sorting subdomains", sorting.sort_file) != 0:
        print("\n[!] Error sorting subdomains.")
        return 1
    print("\n[+] Subdomains sorted successfully.")
    return 0




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Subdomain Enumeration Tool")
    parser.add_argument("-u", "--url", required=True, help="Target URL for subdomain enumeration")
    args = parser.parse_args()
    run_subdomain_enum(args.url)
    sort_subdomains()

