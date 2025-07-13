import subprocess
import argparse
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich import box

console = Console()


def run_ffuf(url, wordlist, others=None):
    cmd = ['ffuf', '-u', f'{url}/FUZZ', '-w', wordlist]
    if others:
        cmd.extend(others.split())
    
    console.print(Panel.fit("[bold cyan]Starting dir scan...[/bold cyan]", box=box.DOUBLE))
    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                line = output.strip()
                
                if '[Status:' in line:
                    print(line)
        rc = process.poll()
        return rc
    except subprocess.CalledProcessError as e:
        print(f"[❌] Error running ffuf: {e}")
        return 1

