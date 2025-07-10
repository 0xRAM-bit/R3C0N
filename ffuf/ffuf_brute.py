import subprocess
import argparse
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich import box

console = Console()

# def run_ffuf(url, wordlist, others=None):
#     cmd = ['ffuf', '-u', f'{url}/FUZZ', '-w', wordlist]
#     if others:
#         cmd.extend(others.split())
    
#     console.print(Panel.fit("[bold cyan]Starting FFUF scan...[/bold cyan]", box=box.DOUBLE))
#     try:
#         process = subprocess.Popen(
#             cmd,
#             stdout=subprocess.PIPE,
#             stderr=subprocess.STDOUT,
#             text=True
#         )

#         # Wait for the process to complete and capture output
#         output, _ = process.communicate()

#         # Print full output
#         for line in output.splitlines():
#             print(line)

#         return process.returncode

#     except subprocess.CalledProcessError as e:
#         print(f"[❌] Error running ffuf: {e}")
#         return 1

def run_ffuf(url, wordlist, others=None):
    cmd = ['ffuf', '-u', f'{url}/FUZZ', '-w', wordlist]
    if others:
        cmd.extend(others.split())
    
    console.print(Panel.fit("[bold cyan]Starting FFUF scan...[/bold cyan]", box=box.DOUBLE))
    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        # Only print lines that look like results, not progress or comments
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                line = output.strip()
                # Filter: print only lines with [Status: ...]
                if '[Status:' in line:
                    print(line)
        rc = process.poll()
        return rc
    except subprocess.CalledProcessError as e:
        print(f"[❌] Error running ffuf: {e}")
        return 1
# Example usage:
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description='Run ffuf for directory brute-forcing.')
#     parser.add_argument('-u', help='Target URL (e.g., http://example.com)')
#     parser.add_argument('-w', help='Path to the wordlist file')
#     parser.add_argument('--others', help='use it like --others "option1 option2 .."', default=None)

#     args = parser.parse_args()

#     result = run_ffuf(args.u, args.w, args.others)

#     if result == 0:
#         print("[✅] ffuf completed successfully.")
#     else:
#         print("[❌] ffuf encountered an error.")

