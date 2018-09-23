#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
from wakeonlan import wol


def main(args):
    ping_response = os.system('ping -c 1 -w 5000 %s' % args.ipaddress[0])
    if ping_response == 0:
        print('%s is responding' % args.ipaddress[0])
    else:
        print('%s is not responding, ask for wake up' % args.ipaddress[0])
        wol.send_magic_packet(args.macaddress[0])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ping and wake on lan if failur                                                                                                             e')
    parser.add_argument('ipaddress', metavar='IPAddr', type=str, nargs=1,
                    help='IP Address to ping')
    parser.add_argument('macaddress', metavar='MAC', type=str, nargs=1,
                    help='MAC Address to wake up')
    args = parser.parse_args()
    main(args)
