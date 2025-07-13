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

def get_colored_categories():
    return "\n".join([f"{color}{cat}{reset}" for cat, color in payload_categories])

def load_payload_file(keyword):
    if keyword == "filter_bypass":
        path = "xss/filter_bypass.json"
    elif keyword == "polyglot":
        path = "xss/polyglot_xss.json"
    elif keyword == "WAF_bypass":
        path = "xss/waf_bypass.json"
    elif keyword == "csp_bypass":
        path = "xss/csp_bypass.json"
    elif keyword == "generic":
        path = "xss/generic.json"
    #------------------ SQL INjection ----------------------------------------
    elif keyword == "sqli_generic":
        path = "sqli/generic.json"
    elif keyword == "mysql":
        path = "sqli/mysql.json"
    elif keyword == "postgres":
        path = "sqli/postgres.json"
    #------------------ SSTI injection ----------------------------------------
    elif keyword == "asp":
        path = "ssti/asp.json"
    elif keyword == "java":
        path = "ssti/java.json"
    else:
        path = f"payloads/{keyword}.json"
    try:
        with open(path, 'r') as f:
            data = json.load(f)
            return data["payloads"]
    except FileNotFoundError:
        return []

def main():
    parser = argparse.ArgumentParser(
        description="Payload Finder CLI for Web Application Testing"
    )

    parser.add_argument(
        '-p', '--payload', required=True, choices=[cat for cat, _ in payload_categories],
        help=f"Payload category:\n{get_colored_categories()}"
    )

    parser.add_argument(
        '-t', '--tech',
        help=(
            "Subtype / Technology:\n\n"
            "For XSS:\n"
            "  filter_bypass, polyglot, WAF_bypass, csp_bypass, generic\n\n"
            "\nFor SQLi:\n"
            "  mysql, postgres, generic, auth_bypass, time_based, polyglot"
        )
    )

    args = parser.parse_args()

    if args.payload == "xss":
        if args.tech == "filter_bypass":
            payls = load_payload_file("filter_bypass")
        elif args.tech == "polyglot":
            payls = load_payload_file("polyglot")
        elif args.tech == "WAF_bypass":
            payls = load_payload_file("WAF_bypass")
        elif args.tech == "csp_bypass":
            payls = load_payload_file("csp_bypass")
        elif args.tech == "generic":
            payls = load_payload_file("generic")
        elif args.tech:
            payls = load_payload_file(args.tech)
        else:
            payls = load_payload_file("xss")

    elif args.payload == "sqli":
        payls = []

        if args.tech == "mysql":
            payls = load_payload_file("mysql")
        elif args.tech == "postgres":
            payls = load_payload_file("postgres")
        elif args.tech == "generic":
            payls = load_payload_file("sqli_generic")

        if args.tech == "auth_bypass":
            path_sql = "sqli/auth_bypass.txt"
        elif args.tech == "time_based":
            path_sql = "sqli/time_based.txt"
        elif args.tech == "polyglot":
            path_sql = "sqli/SQLi_Polyglots.txt"
        else:
            path_sql = None

        if path_sql:
            with open(path_sql, "r") as f:
                data = f.readlines()
            for i in data:
                payload = i.strip()
                if payload:
                    print(f"\033[92m[{args.tech}] \033[91m[{payload}]\033[0m")
    #---------------SSTI----------------------------------------
    elif args.payload == "ssti":
        if args.tech == "asp":
            payls = load_payload_file("asp")
        if args.tech == "java":
            payls_java = load_payload_file("java")
            if payls_java:
                for q in payls_java:
                    print(f"\033[92m[{q.get('type', '?')}] \033[94m[{q.get('tech', '?')}] \033[91m[{q.get('payload', '?')}]\033[0m")
        
            

    else:
        payls = load_payload_file(args.payload)

    if payls:
        for p in payls:
            print(f"\033[92m[{p.get('type', '?')}] \033[91m[{p.get('payload', '?')}]\033[0m")

if __name__ == "__main__":
    main()
