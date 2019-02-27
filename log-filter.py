import argparse
import sys
import iptools

def validate(ip):
    return iptools.ipv4.validate_ip(ip)

def filter(ip):
    for line in sys.stdin:
        if line.split()[0] == ip:
            print(line, end='')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Filter access logs by IP address')
    parser.add_argument('--ip', dest='ip', help='IP address')

    args = parser.parse_args()

    if not validate(args.ip):
         sys.exit('IP invalid. Exiting.')

    filter(args.ip)
