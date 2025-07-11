import json, argparse

colors = {
    "xss": "\033[91m",            # Red
    "sqli": "\033[93m",           # Yellow
    "ssti": "\033[96m",           # Cyan
    "crlf": "\033[95m",           # Magenta
    "403_bypass": "\033[92m",     # Green
    "lfi": "\033[94m",            # Blue
    "upload_bypass": "\033[95m",  # Light Magenta
    "rce": "\033[97m",            # Bright White
}

reset = "\033[0m"

payload_categories = [
    ("xss", colors["xss"]),
    ("sqli", colors["sqli"]),
    ("ssti", colors["ssti"]),
    ("crlf", colors["crlf"]),
    ("403_bypass", colors["403_bypass"]),
    ("lfi", colors["lfi"]),
    ("upload_bypass", colors["upload_bypass"]),
    ("rce", colors["rce"]),
]
reset = "\033[0m"

payload_categories = [
    ("xss", colors["xss"]),
    ("sqli", colors["sqli"]),
    ("ssti", colors["ssti"]),
    ("crlf", colors["crlf"]),
    ("403_bypass", colors["403_bypass"]),
    ("lfi", colors["lfi"]),
    ("upload_bypass", colors["upload_bypass"]),
    ("rce", colors["rce"]),
]

def get_colored_categories():
    return "\n".join([f"{color}{cat}{reset}" for cat, color in payload_categories])

def load_payload_file(keyword):
    # Special case for filter_bypass.json in root
    if keyword == "filter_bypass":
        path = "xss/filter_bypass.json"
    elif keyword == "polyglot":
        path = "xss/polyglot_xss.json"
    elif keyword =="WAF_bypass":
        path = "xss/waf_bypass.json"
    elif keyword == "csp_bypass":
        path = "xss/csp_bypass.json"
    elif keyword == "generic":
        path = "xss/generic.json"
    # else:
    #     path = os.path.join("payloads", f"{keyword}.json")
    with open(path, 'r') as f:
        data = json.load(f)
        return data["payloads"]

def main():
    parser = argparse.ArgumentParser()
    def get_colored_categories():
        return "\n".join([f"{color}{cat}{reset}" for cat, color in payload_categories])
    parser.add_argument(
        '-p','--payload', required=True,
        help=f"Payload category \n" + get_colored_categories()
    )
    parser.add_argument('-t','--tech', help='Technology or subtype (angularjs, filter_bypass, …)')
    args = parser.parse_args()

    if args.payload == "filter_bypass" or args.tech == "filter_bypass":
        payls = load_payload_file("filter_bypass")
    elif args.payload == "polyglot":
        payls = load_payload_file("polyglot")
    elif args.payload == "WAF_bypass":
        payls = load_payload_file("WAF_bypass")
    elif args.payload == "csp_bypass":
        payls = load_payload_file("csp_bypass")
    elif args.payload == "generic":
        payls = load_payload_file("generic")
    elif args.tech:
        payls = load_payload_file(args.tech)
    else:
        payls = load_payload_file(args.payload)

    if not payls or len(payls) == 0:
        print("No payloads found.")
        return

    for p in payls:
        print(f"\033[92m[{p.get('type', '?')}] \033[91m{p.get('payload', '?')}\033[0m")

if __name__ == "__main__":
    main()
