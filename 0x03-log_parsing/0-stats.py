#!/usr/bin/python3

import sys
import signal

''' Initialize metrics '''
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_metrics():
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def signal_handler(sig, frame):
    print_metrics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        if len(parts) != 9:
            continue
        
        ip, _, _, date, request, status_code, file_size = parts[0], parts[1], parts[2], parts[3], parts[5], parts[6], parts[8]
        
        try:
            status_code = int(status_code)
            file_size = int(file_size)
            if status_code in status_codes:
                status_codes[status_code] += 1
            total_size += file_size
        except ValueError:
            continue
        
        if line_count % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    print_metrics()
    sys.exit(0)