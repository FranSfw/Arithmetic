class User:
    def __init__(self, id, username, password, status: bool):
        self.id = id
        self.username = username
        self.password = password
        self.status = status

    def __str__(self):
        return f"User(id={self.id}, username={self.username}, status={self.status})"
    

class Operation:
    def __init__(self, id, type, cost):
        self.id = id
        self.type = type
        self.cost = cost

    def __str__(self):
        return f"Operation(id={self.id}, type={self.type}, cost={self.cost})"
    
class Record:
    def __init__(self, id, operation_id, user_id, amount, user_balance, operation_response, date):
        self.id = id
        self.operation_id = operation_id
        self.user_id = user_id
        self.amount = amount
        self.user_balance = user_balance
        self.operation_response = operation_response
        self.date = date
    
    def __str__(self):
        return f"Record(id={self.id}, operation_id={self.operation_id}, user_id={self.user_id}, amount={self.amount}, user_balance={self.user_balance}, operation_response={self.operation_response}, date={self.date})"
    
    
        