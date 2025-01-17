import subprocess
import ctypes
import sys

def is_admin():
    """Check if the user has administrative privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def sync_time_with_internet():
    """Synchronize system clock with internet time servers."""
    try:
        # Use the w32tm command to sync time with internet servers
        subprocess.check_call("w32tm /resync", shell=True)
        print("System time synchronized successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to synchronize time. Error: {e}")

def main():
    if not is_admin():
        print("This script requires administrative privileges to run.")
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:
        sync_time_with_internet()

if __name__ == "__main__":
    main()