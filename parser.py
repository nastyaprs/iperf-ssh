import re

REGEXP = r'\[\s*\d*\]\s*([\d\.-]*)\s*sec\s*([\d\.]*)\s*.Bytes\s*([\d\.]*)\s*.bits/sec'

def parse_iperf_output(output):
    match = re.search(REGEXP, output)
    if match:
        return {
            'Transfer': float(match.group(2)),  # Transfer в MB
            'Bitrate': float(match.group(3))  # Bitrate в Mbit/s
        }
    return None
