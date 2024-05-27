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
    
    