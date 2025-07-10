import subprocess


class Sorting:
    def __init__(self, f1, f2):
        self.f1 = f1
        self.f2 = f2

    def sort_file(self):
        # Use shell=True for the pipe and redirection, but pass the command as a string
        cmd = f"sort {self.f1} {self.f2} | uniq -u > sorted_subs.txt"
        try:
            subprocess.run(cmd, check=True, shell=True)
            return 0
        except subprocess.CalledProcessError as e:
            print(f"\n[!] Error sorting files: {e}")
            return 1
        except FileNotFoundError:
            print("\n[!] Sort command not found. Please install it.")
            return 1
        except Exception as e:
            print(f"\n[!] Unexpected error in sorting: {e}")
            return 1

# Example usage:
# a = Sorting('asset.txt', 'subfinder.txt')
# a.sort_file()