def run_nmap(target):
    import nmap
    import csv
    import io
    from rich.console import Console
    from rich.table import Table

    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments='-A')
    csv_output = nm.csv()
    csv_reader = csv.DictReader(io.StringIO(csv_output), delimiter=';')
    sorted_rows = sorted(csv_reader, key=lambda row: int(row['port']) if row['port'].isdigit() else 0)

    console = Console()
    table = Table(title="📡 Nmap Scan Results", show_lines=True)
    table.add_column("Port", style="bold yellow", justify="right")
    table.add_column("Host", style="cyan")
    table.add_column("Hostname", style="cyan")
    table.add_column("Protocol", style="green")
    table.add_column("Name", style="bright_green")
    table.add_column("State", style="green")
    table.add_column("Product", style="magenta")
    table.add_column("Extra Info", style="magenta")
    table.add_column("Reason", style="blue")
    table.add_column("Version", style="blue")
    table.add_column("Conf", style="white")
    table.add_column("CPE", style="red")

    for row in sorted_rows:
        table.add_row(
            row['port'], row['host'], row['hostname'], row['protocol'],
            row['name'], row['state'], row['product'], row['extrainfo'],
            row['reason'], row['version'], row['conf'], row['cpe']
        )

    console.print(table)
