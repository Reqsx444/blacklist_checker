# blacklist_checker
Skrypt służy do weryfikowania występowania adresów IP na najpopularniejszych BL. Dzięki zastosowaniu asynchronicznych zadań jest w stanie sprawdzić dużą ilość adresów w krótkim czasie.\
Usprawnieniem, które warto dodać na samym początku jest wyświetlanie BL w pliku końcowym i nie wyświetlanie adresów, które nie występują na BL. W tym celu należy w pliku /usr/local/lib/python3.9/dist-packages/pydnsbl/checker.py zmienić poniższą funkcję:\
    def __repr__(self):\
        blacklisted = '[BLACKLISTED]' if self.blacklisted else ''\
        return "<DNSBLResult: %s %s %s (%d/%d)>" % (self.addr, blacklisted, self.detected_by , len(self.detected_by),\
                                                 len(self.providers))\
