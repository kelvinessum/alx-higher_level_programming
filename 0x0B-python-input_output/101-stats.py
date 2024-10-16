#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics based on log entries.
"""
import sys


def print_metrics(total_size, status_counts):
    """
    Prints the accumulated metrics.

    Args:
        total_size (int): The total file size.
        status_counts (dict): A dictionary with status codes as values.
    """
    print("Total file size: {}".format(total_size))
    for status_code in sorted(status_counts):
        if status_counts[status_code] > 0:
            print("{}: {}".format(status_code, status_counts[status_code]))


def main():
    """
    Main function to read from stdin and compute metrics.
    """
    total_size = 0
    status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    status_counts = {code: 0 for code in status_codes}

    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1

            parts = line.split()
            if len(parts) < 9:
                continue

            status_code = parts[-2]
            file_size = int(parts[-1])

            total_size += file_size

            if status_code in status_counts:
                status_counts[status_code] += 1

            if line_count % 10 == 0:
                print_metrics(total_size, status_counts)

    except KeyboardInterrupt:
        print_metrics(total_size, status_counts)


if __name__ == "__main__":
    main()
