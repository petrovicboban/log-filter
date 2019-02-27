#!/usr/bin/env python3

import argparse
import sys
import iptools


def validate(ip):
    """Check if ip is valid"""
    return iptools.ipv4.validate_ip(ip) or iptools.ipv4.validate_cidr(ip)


def filter(ip):
    """Filter lines on STDIN by ip"""
    if not validate(ip):
         sys.exit('IP or CIDR range invalid. Exiting.')
    for line in sys.stdin:
        if not line.strip():
            continue  # Ignore empty lines
        line_ip = line.split()[0]
        if iptools.ipv4.validate_ip(line_ip) and line_ip in iptools.IpRange(ip):
            yield(line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Filter access logs by IP address or CIDR range')
    parser.add_argument('--ip', dest='ip', help='IP address or CIDR range')
    args = parser.parse_args()


    for line in filter(args.ip):
        print(line, end='')
