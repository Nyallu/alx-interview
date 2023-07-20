#!/usr/bin/python3
import sys
import signal

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def print_stats():
    total_size = sum(file_sizes.values())
    print("File size:", total_size)
    for status_code in sorted(status_codes.keys()):
        print(f"{status_code}: {status_codes[status_code]}")

file_sizes = {}
status_codes = {}

try:
    for line_count, line in enumerate(sys.stdin, 1):
        try:
            _, _, _, _, _, status_code, file_size = line.strip().split()[3:]
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue

        file_sizes[line_count] = file_size
        status_codes[status_code] = status_codes.get(status_code, 0) + 1

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
