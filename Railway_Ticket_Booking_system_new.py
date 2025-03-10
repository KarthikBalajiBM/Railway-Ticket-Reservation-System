class Ticket:
    def __init__(self,ticket_number,passenger_name,passenger_phno,age,berth,price):
        self.ticket_no = ticket_number
        self.passenger_name = passenger_name
        self.passenger_phno = passenger_phno
        self.age = age
        self.berth = berth
        self.price = price

class Train:
    train_id = 1
    def __init__(self,lower_berth,upper_berth,middle_berth,rac,waitinglist,price):
        self.train_id = Train.train_id
        Train.train_id += 1
        self.lower_berth = lower_berth
        self.upper_berth = upper_berth
        self.middle_berth = middle_berth
        self.ticket = lower_berth + upper_berth + middle_berth
        self.rac = rac
        self.waitinglist = waitinglist
        self.tickets = []
        self.price=price
        self.ticket_number=1
    
    def suggest_Ticket(self):
        print("Your berth preference is not available")
        if self.ticket > 0:
            if self.lower_berth > 0:
                print("Lower berth is available")
                print("Enter 1 to book lower berth")
                
            if self.upper_berth > 0:
                print("Upper berth is available")
                print("Enter 2 to book upper berth")
                
            if self.middle_berth > 0:
                print("Middle berth is available")  
                print("Enter 3 to book middle berth")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.lower_berth -= 1
                return True,"lower"
            elif choice == 2:
                self.upper_berth -= 1
                return True,"upper"
            elif choice == 3:
                self.middle_berth -= 1
                return True,"middle"
            else:
                return False,""
            
        elif self.rac > 0:
            print("RAC is available")
            print("Enter yes/no to book RAC")
            choice = input("Enter your choice: ")
            if choice == "yes":
                self.rac -= 1
                return True,"rac"
            else:
                return False,""
        elif self.waitinglist > 0:
            print("Waitinglist is available")
            print("Enter yes/no to book waitinglist")
            choice = input("Enter your choice: ")
            if choice == "yes":
                self.waitinglist -= 1
                return True,"waitinglist"
            else:
                return False,""
            
    def book_ticket(self):

        a=int(input("Enter the number of tickets to book: "))
        total_price=0
        for j in range(a):
            passenger_name = input("Enter the passenger name: ")
            passenger_phno = input("Enter the passenger phone number: ")
            age = int(input("Enter the passenger age: "))
            berth = input("Enter the berth preference(lower/middle/upper): ")
        

            if berth == "lower":
                if self.lower_berth > 0:
                    self.lower_berth -= 1
                    self.ticket -= 1
                    booked=True
                elif self.ticket > 0 or self.rac > 0 or self.waitinglist > 0:
                    booked,berth=self.suggest_Ticket()
            elif berth == "upper":
                if self.upper_berth > 0:
                    self.upper_berth -= 1
                    self.ticket -= 1
                    booked=True
                elif self.ticket > 0 or self.rac > 0 or self.waitinglist > 0:
                    booked,berth=self.suggest_Ticket()
            elif berth == "middle":    
                if self.middle_berth > 0:
                    self.middle_berth -= 1
                    self.ticket -= 1
                    booked=True

                elif self.ticket > 0 or self.rac > 0 or self.waitinglist > 0:
                    booked,berth=self.suggest_Ticket()
            
            if booked:
                ticket = Ticket(self.ticket_number,passenger_name,passenger_phno,age,berth,self.price)
                self.tickets.append(ticket)
                total_price+=self.price
                print(f"Ticket booked successfully! Ticket number is {ticket.ticket_no}")
                self.ticket_number+=1
            else:
                print("Ticket booking failed!,Thank you")
                return 

        print("Total price is",total_price)
    
    def cancel_ticket(self):
        ticket_no = int(input("Enter the ticket number to cancel: "))
        name=input("Enter the passenger name: ")
        phno=input("Enter the passenger phone number: ")

        found=False
        for ticket in self.tickets:
            if ticket.ticket_no == ticket_no and ticket.passenger_name==name and ticket.passenger_phno==phno:
                cancelled_ticket=ticket
                self.tickets.remove(ticket)
                print(f"Ticket number {ticket_no} is cancelled successfully! and refunded price is {ticket.price}")
                found=True
                break
        if not found:
            print("Ticket not found!")
            return
        if cancelled_ticket.berth=="lower":
            changed=self.change_ticket_rac_and_waiting(cancelled_ticket.berth)
            if not changed:
                self.lower_berth+=1
                self.ticket+=1
        elif cancelled_ticket.berth=="upper":
            changed=self.change_ticket_rac_and_waiting(cancelled_ticket.berth)
            if not changed:
                self.upper_berth+=1
                self.ticket+=1
        elif cancelled_ticket.berth=="middle":
            changed=self.change_ticket_rac_and_waiting(cancelled_ticket.berth)
            if not changed:
                self.middle_berth+=1
                self.ticket+=1
        elif cancelled_ticket.berth=="rac":
            changed=self.change_ticket_waiting(cancelled_ticket.berth)
            if not changed:
                self.rac+=1
        elif cancelled_ticket.berth=="waitinglist":
            self.waitinglist+=1
    

    def change_ticket_waiting(self,berth):
        found_waitinglist=False
        for ticket in self.tickets:
            if ticket.berth=="waitinglist":
                ticket.berth=berth
                found_waitinglist=True
                break
        if not found_waitinglist:
            return False       
        return True
        
            
    def change_ticket_rac_and_waiting(self,berth):
        found_rac=False
        for ticket in self.tickets:
            if ticket.berth=="rac":
                ticket.berth=berth
                found_rac=True
                break
        found_waitinglist=False
        if not found_rac:
            for ticket in self.tickets:
                if ticket.berth=="waitinglist":
                    ticket.berth=berth
                    found_waitinglist=True
                    break
        if not found_rac and not found_waitinglist:
            return False       
        return True

class Railways:
    def __init__(self):
        self.trains = []

Railway = Railways()

n=int(input("Enter the number of trains: "))
for i in range(n):
    print(f"Number of berth in train {i+1}")
    lower_berth = int(input("Enter the number of lower berth: "))
    upper_berth = int(input("Enter the number of upper berth: "))
    middle_berth = int(input("Enter the number of middle berth: "))
    rac = int(input("Enter the number of rac: "))
    waitinglist = int(input("Enter the number of waitinglist: "))
    price = int(input("Enter the price of ticket: "))
    train = Train(lower_berth,upper_berth,middle_berth,rac,waitinglist,price)
    Railway.trains.append(train)

while True:
    print("1. Exit")
    print("2. Book Ticket")
    print("3. Cancel Ticket")
    print("4. Print Ticket")
    print("5. No of tickets available")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        break
    elif choice == 2:
        train_id = int(input("Enter the train id: "))
        for i in Railway.trains:
            if i.train_id == train_id:
                train = i
                break
        train.book_ticket()       


    elif choice == 3:
        train_id = int(input("Enter the train id: "))
        for i in Railway.trains:
            if i.train_id == train_id:
                train = i
                break
        train.cancel_ticket()
        
    elif choice == 4:
        train_id = int(input("Enter the train id: "))
        for i in Railway.trains:
            if i.train_id == train_id:
                train = i
                break
        ticket_no = int(input("Enter the ticket number to print: "))
        for i in train.tickets:
            if i.ticket_no == ticket_no:
                ticket = i
                break
        print("Ticket details")
        print(f"Ticket number: {ticket_no}")
        print(f"Passenger name: {ticket.passenger_name}")
        print(f"Passenger phone number: {ticket.passenger_phno}")
        print(f"Passenger age: {ticket.age}")
        print(f"Berth preference: {ticket.berth}")
        print(f"Price: {ticket.price}")

    elif choice == 5:
        print("Number of tickets available")
        for train in Railway.trains:
            print(f"Train ID: {train.train_id}")
            print(f"Lower berth: {train.lower_berth}")
            print(f"Upper berth: {train.upper_berth}")
            print(f"Middle berth: {train.middle_berth}")
            print(f"RAC: {train.rac}")
            print(f"Waitinglist: {train.waitinglist}")
    else:
        print("Invalid choice! Please enter a valid choice.")



