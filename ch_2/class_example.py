class Transaction:
    def __init__(self, amount, user):
        self._amount = amount
        self._user = user
    
    def get_amount( self ):
        return self._amount
    
    def get_user( self ):
        return self._user


new_transaction = Transaction( 5, 'person')

print( new_transaction.get_amount() )
print( new_transaction.get_user() )
