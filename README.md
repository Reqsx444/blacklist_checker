# blacklist_checker
The script is used to verify whether IP addresses occur on the most popular BLs. Utilizing asynchronous tasks, it is able to check a large number of addresses in a short period of time.
An enhancement worth considering from the outset is to display the BL in the final output file and not display addresses that do not appear on the BL. To achieve this, modify the following function in the file /usr/local/lib/python3.9/dist-packages/pydnsbl/checker.py:
    def __repr__(self):\
        blacklisted = '[BLACKLISTED]' if self.blacklisted else ''\
        return "<DNSBLResult: %s %s %s (%d/%d)>" % (self.addr, blacklisted, self.detected_by , len(self.detected_by),\
                                                 len(self.providers))\
