from tabulate import tabulate
import time
from rich.console import Console
console = Console()
console.clear()
print(r"""Developed By:
  __   ___    ______       _  _          ______        ___  
 /_ | |__ \  |____  |     | || |        |____  |      / _ \ 
  | |    ) |     / /      | || |_           / /      | (_) |
  | |   / /     / /       |__   _|         / /        > _ < 
  | |  / /_    / /     _     | |     _    / /     _  | (_) |
  |_| |____|  /_/     (_)    |_|    (_)  /_/     (_)  \___/""")
time.sleep(2.5)
def print_command_info():
    commands = [
        ("ssh", "Secure Shell; used to securely connect to a remote server or machine."),
        ("ls", "Lists the contents of a directory."),
        ("pwd", "Prints the working directory; shows the current directory path."),
        ("cd", "Changes the current directory."),
        ("touch", "Creates an empty file or updates the timestamp of an existing file."),
        ("echo", "Displays a line of text or variable value to the terminal."),
        ("nano", "A simple text editor for editing files directly from the terminal."),
        ("vim", "A highly configurable text editor with powerful features."),
        ("cat", "Concatenates and displays file contents."),
        ("shred", "Overwrites a file multiple times to securely delete it."),
        ("mkdir", "Creates a new directory."),
        ("cp", "Copies files or directories from one location to another."),
        ("rm", "Removes (deletes) files or directories."),
        ("rmdir", "Removes empty directories."),
        ("ln", "Creates hard or symbolic links to files or directories."),
        ("clear", "Clears the terminal screen."),
        ("whoami", "Displays the current user’s username."),
        ("useradd", "Adds a new user to the system."),
        ("sudo", "Executes a command with superuser (root) privileges."),
        ("adduser", "Adds a new user and sets up their account."),
        ("su", "Switches the current user to another user, typically the root user."),
        ("exit", "Exits the current shell or terminal session."),
        ("passwd", "Changes the password for a user account."),
        ("apt", "Package management command used to handle packages in Debian-based systems."),
        ("finger", "Displays information about users on the system."),
        ("man", "Displays the manual page for a command."),
        ("whatis", "Provides a short description of a command or function."),
        ("curl", "Transfers data from or to a server using various protocols (e.g., HTTP, FTP)."),
        ("zip", "Compresses files into a ZIP archive."),
        ("unzip", "Extracts files from a ZIP archive."),
        ("less", "Views file contents one screen at a time, allowing backward and forward navigation."),
        ("head", "Displays the first few lines of a file."),
        ("tail", "Displays the last few lines of a file."),
        ("cmp", "Compares two files byte by byte."),
        ("diff", "Compares files line by line and shows differences."),
        ("sort", "Sorts lines of text files."),
        ("find", "Searches for files and directories in a directory hierarchy."),
        ("chmod", "Changes the permissions of a file or directory."),
        ("chown", "Changes the ownership of a file or directory."),
        ("ifconfig", "Displays or configures network interface parameters (older tool, often replaced by ip)."),
        ("ip address", "Displays or configures IP addresses on network interfaces."),
        ("grep", "Searches for patterns within files."),
        ("awk", "A powerful text processing and data extraction tool."),
        ("resolvectl status", "Displays the status of DNS resolver."),
        ("ping", "Tests network connectivity to a host."),
        ("netstat", "Displays network connections, routing tables, and network statistics."),
        ("ss", "Provides detailed information about network sockets."),
        ("iptables", "Configures IP packet filtering rules (used for setting up firewalls)."),
        ("ufw", "Uncomplicated Firewall; simplifies firewall management on Linux systems."),
        ("uname", "Displays system information, such as the kernel version and architecture."),
        ("neofetch", "Displays system information and statistics in a visually appealing way."),
        ("cal", "Displays a calendar."),
        ("free", "Shows memory usage, including total, used, and available memory."),
        ("df", "Displays disk space usage for file systems."),
        ("ps", "Displays information about running processes."),
        ("top", "Provides a real-time view of system processes and resource usage."),
        ("htop", "An interactive process viewer with a more user-friendly interface compared to top."),
        ("kill", "Sends a signal to terminate a process."),
        ("pkill", "Sends a signal to terminate processes based on name or other attributes."),
        ("systemctl", "Controls and manages systemd services and the system state."),
        ("history", "Shows the command history of the terminal session."),
        ("reboot", "Restarts the system."),
        ("shutdown", "Shuts down the system.")
    ]
    
    headers = ["Command", "Description"]
    table = tabulate(commands, headers=headers, tablefmt="grid")
    
    print(table)
    input("Press Enter to exit...")

if __name__ == "__main__":
    print_command_info()
