import requests
import argparse
from termcolor import colored

# Function to display a friendly banner
def show_banner():
    print(colored("  Welcome to VFuzzer!", 'green'))
    print(colored("  Let's Find Some Vhosts!", 'green'))
    print(colored("  ======================", 'green'))

# Function to find virtual hosts
def find_vhosts(target_domain, wordlist):
    try:
        with open(wordlist, 'r') as file:
            for line in file:
                vhost = line.strip()
                url = f'http://{vhost}.{target_domain}'
                try:
                    response = requests.get(url)
                    if response.status_code == 200:
                        print(colored(f"Found Vhost: {vhost}.{target_domain}", 'green'))
                except requests.exceptions.RequestException:
                    pass  # Ignore connection errors
    except FileNotFoundError:
        print(colored("Wordlist not found!", 'red'))

# Main script execution
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="VFuzzer - Vhost Enumeration Tool")
    parser.add_argument("-d", "--domain", help="Specify the target domain for vhost enumeration")
    parser.add_argument("-w", "--wordlist", help="Provide the path to the wordlist file")

    args = parser.parse_args()

    # Display the friendly banner
    show_banner()

    # Check for missing arguments
    if not args.domain:
        print(colored("Please provide the target domain using -d option.", 'red'))
    elif not args.wordlist:
        print(colored("Don't forget to specify the wordlist file using -w option.", 'red'))
    else:
        print(colored("Scanning for vhosts...", 'green'))
        find_vhosts(args.domain, args.wordlist)

