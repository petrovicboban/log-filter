#!/usr/bin/env python3

import argparse
import sys
import iptools


def validate(ip):
    """Check if ip is valid"""
    return iptools.ipv4.validate_ip(ip) or iptools.ipv4.validate_cidr(ip)


def filter(ip):
    """Filter lines on STDIN by ip"""
    for line in sys.stdin:
        line_ip = line.split()[0]
        if iptools.ipv4.validate_ip(line_ip) and line_ip in iptools.IpRange(ip):
            print(line, end='')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Filter access logs by IP address or CIDR range')
    parser.add_argument('--ip', dest='ip', help='IP address or CIDR range')
    args = parser.parse_args()

    if not validate(args.ip):
         sys.exit('IP or CIDR range invalid. Exiting.')

    filter(args.ip)
