# IP Address Blacklist Checker Script Description
## Introduction
This script is designed to verify whether specified IP addresses appear on popular blacklists (BLs). Utilizing asynchronous tasks, it efficiently checks a large number of addresses in a short period of time. The results of the checks are saved to a log file, with additional features to clean and format the output.

## Features
Package Verification and Installation: Ensures necessary Python packages are imported and available.
Log Handling: Creates a log file for storing results and removes previous logs to prevent data overlap.
IP Address Handling: Converts CIDR prefixes into individual IP addresses for verification.
Asynchronous Processing: Uses asynchronous functions to speed up the checking process.
Result Logging: Saves the results of IP address checks to a log file, removing empty lines and irrelevant data for clarity.

## Usage
### Prerequisites:
- Python 3
- Libraries: pydnsbl, ipaddress, asyncio, time, os
- 
## Example Usage
python ip_blacklist_checker.py

### BUG
An enhancement worth considering from the outset is to display the BL in the final output file and not display addresses that do not appear on the BL. To achieve this, modify the following function in the file /usr/local/lib/python3.9/dist-packages/pydnsbl/checker.py:
    def __repr__(self):\
        blacklisted = '[BLACKLISTED]' if self.blacklisted else ''\
        return "<DNSBLResult: %s %s %s (%d/%d)>" % (self.addr, blacklisted, self.detected_by , len(self.detected_by),\
                                                 len(self.providers))\
