import argparse
import sys

def main():
    parser = argparse.ArgumentParser(
        description="Ultimate CTF Tool: A collection of tools for CTF players."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Subparser: Port Scanner
    portscan_parser = subparsers.add_parser(
        "portscan",
        help="Run a port scan on a target host"
    )
    portscan_parser.add_argument(
        "-t", "--target",
        required=True,
        help="Target host or IP address to scan"
    )

    # Subparser: Directory Brute-Forcing
    dir_parser = subparsers.add_parser(
        "dir",
        help="Run directory brute-forcing using ffuf"
    )
    dir_parser.add_argument(
        "-u", "--url",
        required=True,
        help="Target URL with FUZZ placeholder"
    )
    dir_parser.add_argument(
        "-w", "--wordlist",
        required=True,
        help="Path to the wordlist"
    )
    dir_parser.add_argument(
        "--others",
        default=None,
        help="Additional ffuf options, e.g. '--others \"-mc 200 -t 100\""
    )


    # Advanced Subdomain Enumeration
    adv_parser = subparsers.add_parser("advrecon", help="Advanced subdomain enumeration")
    adv_parser.add_argument("-d", "--domain", required=True, help="Target domain")
    adv_parser.add_argument("-a", "--api", required=True, help="API key for chaos-client visit https://cloud.projectdiscovery.io")

    # Parameter Finder
    param_parser = subparsers.add_parser("paramfinder", help="Find interesting parameters in URLs")
    param_parser.add_argument("-p", "--param", required=True, help="Parameter set to search for (e.g. xss, sql, ssti, rce, lfi, idor, interesting, js)")
    param_parser.add_argument("-f", "--file", required=True, help="File to search in")

    # Katana Scraper
    katana_parser = subparsers.add_parser("crawl", help="Crawl subdomains")
    katana_parser.add_argument("-f", "--file", required=True, help="File with subdomains")


    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    def spinner(task_name, message, target_func, *args, **kwargs):
        import threading, time
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

    if args.command == "portscan":
        #print(f"Scanning {args.target} with nmap...")
        from nmap_scanner.nmap_scanner import run_nmap
        spinner("Portscan", f"Running nmap on {args.target}", run_nmap, args.target)

    elif args.command == "dir":
        #print(f" Starting directory fuzz on {args.url}...")
        from ffuf.ffuf_brute import FFUF
        ffuf = FFUF()
        spinner("Directory Fuzz", f"Running ffuf on {args.url}", ffuf.run_ffuf, args.url, args.wordlist, args.others)

    elif args.command == "advrecon":
        #print(f"[+] Running advanced subdomain enumeration on {args.domain}...")
        from recon.Advance_recon.adv_subs_scrp import Adv_Subs
        adv_subs = Adv_Subs(args.domain, args.api)
        spinner("Advanced Subdomain Enumeration", f"Running advanced subdomain enumeration on {args.domain}", adv_subs.run_adv_subs)

    elif args.command == "paramfinder":
        #print(f"[+] Finding parameters of type '{args.param}' in '{args.file}'...")
        from recon.intersting_parms_finder.parms_finder import ParmsFinder
        finder = ParmsFinder(args.param, args.file)
        spinner("Parameter Finder", f"Finding parameters in {args.file}", finder.find_parms)

    elif args.command == "crawl":
        #print(f"[+] Scraping subdomains from '{args.file}' with Katana...")
        from recon.scrapper_working.katana import Katana
        katana = Katana(args.file)
        spinner("CRAWL", f"Running crawl on {args.file}", katana.run_katana)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()