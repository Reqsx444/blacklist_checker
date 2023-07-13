# blacklist_checker
Na samym początku należy w pliku /usr/local/lib/python3.9/dist-packages/pydnsbl/checker.py zmienić poniższą funkcję (dodane wyświetlanie BL i nie wyświetlanie adresów, które nie występują na BL)\
    def __repr__(self):
        blacklisted = '[BLACKLISTED]' if self.blacklisted else ''
        return "<DNSBLResult: %s %s %s (%d/%d)>" % (self.addr, blacklisted, self.detected_by , len(self.detected_by),
                                                 len(self.providers))
