# blacklist_checker
The script is used to verify the occurrence of IP addresses on the most popular BLs. By using asynchronous tasks, it is able to check a large number of addresses in a short period of time. \
An enhancement worth adding at the very beginning is to display BL in the final file and not display addresses that do not appear on BL. To do this, change the following function in the file /usr/local/lib/python3.9/dist-packages/pydnsbl/checker.py:\
    def __repr__(self):\
        blacklisted = '[BLACKLISTED]' if self.blacklisted else ''\
        return "<DNSBLResult: %s %s %s (%d/%d)>" % (self.addr, blacklisted, self.detected_by , len(self.detected_by),\
                                                 len(self.providers))\
