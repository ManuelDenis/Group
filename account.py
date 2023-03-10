class Account:
    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions = []
        self.start = 0
        self.end = len(self._transactions)

    def handle_transaction(self, transaction_amount):
        if self.amount + transaction_amount >= 0:
            self.amount += transaction_amount
            self._transactions.append(transaction_amount)
            return f"New balance: {self.amount}"
        else:
            raise ValueError("sorry cannot go in debt!")

    def add_transaction(self, amount):
        if type(amount) != int:
            raise ValueError("please use int for amount")
        else:
            if self.amount + sum(self._transactions) + amount < 0:
                raise ValueError("sorry cannot go in debt!")
            else:
                self._transactions.append(amount)
                return f"New balance: {self.amount + sum(self._transactions)}"

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __len__(self):
        return len(self._transactions)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < len(self._transactions):
            ret = self._transactions[self.start]
            self.start += 1
            return ret
        else:
            raise StopIteration

    def __getitem__(self, item):
        return self._transactions[item]

    def __reversed__(self):
        return self._transactions[::-1]

    def __gt__(self, other):
        return self.balance > other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __add__(self, other):
        new = Account(f"{self.owner}&{other.owner}", self.amount + other.amount)
        new._transactions = self._transactions + other._transactions
        return new
