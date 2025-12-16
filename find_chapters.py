
import re

filename = "extracted_text_utf8.md"
chapters = [
    "Proximity Service",
    "Nearby Friends",
    "Google Maps",
    "Distributed Message Queue",
    "Metrics Monitoring and Alerting System",
    "Ad Click Event Aggregation",
    "Hotel Reservation System",
    "Distributed Email Service",
    "S3-like Object Storage",
    "Real-time Gaming Leaderboard",
    "Payment System",
    "Digital Wallet",
    "Stock Exchange"
]

with open(filename, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")

found = {}
# simple state machine to avoid TOC
# TOC is usually in the first few hundred lines.
# We want the occurrences that look like headings "N Title" or just "Title" on a line by itself or close to it.

for i, line in enumerate(lines):
    line = line.strip()
    for ch in chapters:
        # Match "1 Proximity Service" or "Chapter 1 Proximity Service" or just the title if distinct
        # We'll print all matches with line numbers to manually decide
        if ch in line:
            print(f"{i+1}: {line}")
