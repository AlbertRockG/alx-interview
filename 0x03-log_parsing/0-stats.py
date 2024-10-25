#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""

import sys


def print_status(status_codes, total_size):
    """Prints the accumulated metrics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]))


status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line = line.strip()
        line_count += 1
        parts = line.split()

        try:
            total_size += int(parts[-1])
        except (IndexError, ValueError):
            pass

        try:
            code = parts[-2]
            if code in status_codes:
                status_codes[code] += 1
        except IndexError:
            pass

        if line_count % 10 == 0:
            print_status(status_codes, total_size)

except KeyboardInterrupt:
    print_status(status_codes, total_size)
    raise

print_status(status_codes, total_size)
