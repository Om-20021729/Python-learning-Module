from random import randint

class Train:

    def __init__(self, TrainNo):
        self.TrainNo = TrainNo  # Instance variable

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.TrainNo} from {fro} to {to}")
    
    def getStatus(self, fro, to):
        print(f"Ticket status in train no: {self.TrainNo} from {fro} to {to}")
   
    def getFare(self, fro, to):
        fare = randint(222, 5555)
        print(f"Ticket fare in train no: {self.TrainNo} from {fro} to {to} is {fare}")

# Creating an instance of Train with train number 12662
t = Train(12662)

# Booking a ticket
t.book("SHAHDOL", "BHOPAL")

# Getting ticket status
t.getStatus("SHAHDOL", "BHOPAL")

# Getting ticket fare
t.getFare("SHAHDOL", "BHOPAL")
