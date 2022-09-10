class Securities:
    def __init__(self, security_id, cusip, sedol, isin, ric, bloomberg, bbg, symbol, root_symbol, bb_yellow, spn) -> None:
        self.security_id = security_id
        self.cusip = cusip
        self.sedol = sedol
        self.isin = isin
        self.ric = ric
        self.bloomberg = bloomberg
        self.bbg = bbg
        self.symbol = symbol
        self.root_symbol = root_symbol
        self.bb_yellow = bb_yellow
        self.spn = spn
