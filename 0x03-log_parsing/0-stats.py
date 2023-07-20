#!/usr/bin/python3

import sys

def print_statistics(total_size, status_codes):
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        print(f"{code}: {status_codes[code]}")

def parse_log_line(line):
    try:
        parts = line.strip().split()
        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return ip_address, status_code, file_size
    except (ValueError, IndexError):
        return None, None, None

def main():
    total_size = 0
    status_codes = {}

    try:
        for line_count, line in enumerate(sys.stdin, 1):
            ip, status_code, file_size = parse_log_line(line)
            if ip is None:
                continue

            total_size += file_size
            status_codes[status_code] = status_codes.get(status_code, 0) + 1

            if line_count % 10 == 0:
                print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)
        sys.exit(0)

if __name__ == "__main__":
    main()

