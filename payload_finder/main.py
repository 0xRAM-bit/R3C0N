import argparse
from ssti import SSTI

parser = argparse.ArgumentParser(
        description="Payload Finder CLI for Web Application Testing"
)
parser.add_argument(
        '-p', '--payload', required=True,
        help=f"Payload category:"
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


if args:
    if args.payload == "ssti":
        s = SSTI()
        if args.tech == "asp":
            s.show_payload_ssti_asp()
        elif args.tech == "java":
            s.show_payload_ssti_java()
        else:
            print("please specify the right technology")
    else:
        print("please specify the right payload type")
else:
    print("no args passed please type -h")