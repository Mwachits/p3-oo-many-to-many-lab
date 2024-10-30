class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Invalid book.")
        if not isinstance(date, str) or not isinstance(royalties, int):
            raise Exception("Invalid date or royalties.")
        contract = Contract(author=self, book=book, date=date, royalties=royalties)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return list({contract.author for contract in self.contracts()})


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Invalid author. Must be an instance of Author.")
        if not isinstance(book, Book):
            raise Exception("Invalid book. Must be an instance of Book.")
        if not isinstance(date, str):
            raise Exception("Invalid date. Must be a string.")
        if not isinstance(royalties, int):
            raise Exception("Invalid royalties. Must be an integer.")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]