#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""

import sys
import re

def print_stats(total_size, status_counts):
    """Prints the accumulated metrics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code]:
            print("{}: {}".format(code, status_counts[code]))

status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
status_counts = dict.fromkeys(status_codes, 0)
total_size = 0
line_count = 0

# Regular expression pattern to parse the log lines
log_pattern = re.compile(
    r'(?P<ip>\S+) - \[(?P<date>.*?)\] "(?P<request>GET \/projects\/260 HTTP\/1\.1)" '
    r'(?P<status_code>\d{3}) (?P<file_size>\d+)'
)

try:
    for line in sys.stdin:
        line = line.strip()
        line_count += 1

        # Match the line against the pattern
        match = log_pattern.fullmatch(line)
        if match:
            status_code = match.group('status_code')
            file_size = int(match.group('file_size'))

            # Update the total file size
            total_size += file_size

            # Update the count for the status code
            if status_code in status_counts:
                status_counts[status_code] += 1

        if line_count % 10 == 0:
            print_stats(total_size, status_counts)

except KeyboardInterrupt:
    print_stats(total_size, status_counts)
    raise

# Print any remaining stats after EOF
print_stats(total_size, status_counts)
