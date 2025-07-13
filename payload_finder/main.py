import argparse
from payload_finder import SSTI, XSS, SQLI, Bypass_403_401, CRLF_INJECTION

parser = argparse.ArgumentParser(
        description="Payload Finder CLI for Web Application Testing"
)
parser.add_argument(
        '-p', '--payload', required=True,
        help=f"Payload category: \033[94mssti, xss, sqli, crlf, 403_bypass, upload_bypass\033[0m"
)

parser.add_argument(
        '-t', '--tech',
        help=(
            "Subtype / Technology:\n\n"
            "For \033[91mxss\033[0m:\n"
            "  \033[92m{filter_bypass, polyglot, WAF_bypass, csp_bypass, generic}\033[0m\n\n"
            "\nFor \033[91msqli\033[0m:\n"
            "  \033[92m{mysql, postgres, generic, auth_bypass, time_based, polyglot}\033[0m\n\n"
            "For \033[91mssti\033[0m:\n"
            "  \033[92m{asp, java, javascript, php, python}\033[0m\n\n"
            "use one by one"
        )
)
args = parser.parse_args()


if args.payload == "ssti":
    s = SSTI()
    if args.tech:
        s.show_payload(args.tech)
    else:
        print("Please specify the technology for SSTI: asp, java")

elif args.payload == "xss":
    x = XSS()
    if args.tech:
        x.show_payload(args.tech)
    else:
        print("Please specify the technology for XSS")

elif args.payload == "sqli":
    s = SQLI()
    if args.tech:
        s.show_payload(args.tech)
    else:
        print("Please specify the technology for SQLI")
elif args.payload == "403_bypass":
    bypass_403_401 = Bypass_403_401()
    bypass_403_401.show_payload()
elif args.payload == "upload_bypass":
    print("\033[91m[Please go throught this website for file upload bypass tricks] \n\033[92m[https://book.hacktricks.wiki/en/pentesting-web/file-upload/index.html]\033[0m")
elif args.payload == "crlf":
    crlf_i = CRLF_INJECTION()
    crlf_i.show_payload()
else:
    print("please specify the right payload type")
