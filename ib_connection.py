from ib_insync import IB

class IBConnection:
    def __init__(self):
        self.ib = IB()

    def connect(self):
        try:
            self.ib.connect('127.0.0.1', 7497, clientId=1)
            return True
        except Exception as e:
            print(f"Failed to connect: {e}")
            return False

    def get_connection(self):
        return self.ib
