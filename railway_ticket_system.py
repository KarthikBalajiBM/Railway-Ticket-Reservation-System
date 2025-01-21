class Passenger:
    def __init__(self,name,age,gender,berth):
        self.name=name
        self.age=age
        self.gender=gender
        self.berth=berth

class rtrs:

    def __init__(self):
        self.totalBerth = 3
        self.lowerBerth = 1
        self.middleBerth = 1
        self.upperBerth = 1
        self.totalRac = 1
        self.totalWaitingList = 1

        self.bookedTickets = []
        self.RACTickets = []
        self.waitingListTickets = []

    def suggestion(self):
        
        if self.lowerBerth>0:
            suggested='lower'
        elif self.middleBerth>0:
            suggested='middle'
        elif self.upperBerth>0:
            suggested='upper'
        elif self.totalRac>0:
            suggested='Rac'
        elif self.totalWaitingList>0:
            suggested='waiting'
        else:
            suggested=None
        return suggested
    
    def printAvailableTicket(self):
        print(f'Available are')
        print(f'Lower Berth : {self.lowerBerth}')
        print(f'Middle Berth : {self.middleBerth}')
        print(f'Upper Berth : {self.upperBerth}')
        print(f'RAC : {self.totalRac}')
        print(f'Waiting List : {self.totalWaitingList}')

    def printBookedTicket(self):
        if len(self.bookedTickets):
            print("Booked Tickets are")
            for i in self.bookedTickets:
                print(f'name {i.name}')
                print(f'age {i.age}')
                print(f'gender {i.gender}')
                print(f'berth {i.berth}')
                print()
        
        if len(self.RACTickets):
            print("Rac Tickets are")
            for i in self.RACTickets:
                print(f'name {i.name}')
                print(f'age {i.age}')
                print(f'gender {i.gender}')
                print(f'berth {i.berth}')
                print()
        
        if len(self.waitingListTickets):
            print("Waiting list Tickets are")
            for i in self.waitingListTickets:
                print(f'name {i.name}')
                print(f'age {i.age}')
                print(f'gender {i.gender}')
                print(f'berth {i.berth}')
                print()

    def cancelTicket(self):

        if len(self.bookedTickets)==0 and len(self.RACTickets)==0 and len(self.waitingListTickets)==0:
            print("No Tickets to Cancel")
            return
        name_of_passenger=input("Enter name of the passenger to cancel: ")
        type_of_ticket=input("Enter the type of ticket booked to cancel (Confirmed/RAC/Waiting):").lower()
        found=0
        if type_of_ticket=="waiting":
            for i in range(len(self.waitingListTickets)):
                if self.waitingListTickets[i].name==name_of_passenger:
                    found=1
                    self.waitingListTickets.pop(i)
                    self.totalWaitingList+=1
                    break

        elif type_of_ticket=="rac":
            for i in range(len(self.RACTickets)):
                if self.RACTickets[i].name==name_of_passenger:
                    found=1
                    canceled=self.RACTickets.pop(i)
                    if len(self.waitingListTickets):
                        added_to_rac=self.waitingListTickets.pop(0)
                        added_to_rac.berth="Rac"
                        self.RACTickets.append(added_to_rac.berth)
                        self.totalWaitingList+=1
                    else:
                        self.totalRac+=1
                    break

        elif type_of_ticket=="confirmed":
            for i in range(len(self.bookedTickets)):
                if self.bookedTickets[i].name==name_of_passenger:
                    found=1
                    canceled=self.bookedTickets.pop(i)
                    
                    if len(self.RACTickets):
                        added_to_booked=self.RACTickets.pop(0)
                        added_to_booked.berth=canceled.berth
                        self.bookedTickets.append(added_to_booked)

                        if len(self.waitingListTickets):
                            added_to_rac=self.waitingListTickets.pop(0)
                            added_to_rac.berth='Rac'
                            self.RACTickets.append(added_to_rac)
                            self.totalWaitingList+=1
                        else:
                            self.totalRac+=1
                    else:
                        self.totalBerth+=1
                    
                    if canceled.berth=="upper":
                        self.upperBerth+=1
                    elif canceled.berth=="middle":
                        self.middleBerth+=1
                    elif canceled.berth=="lower":
                        self.lowerBerth+=1
                    break
        if found==0:
            print("Ticket not found")
        else:
            print("Cancelled Successfully")
        return 
    
    def bookTicket(self):
        if self.totalWaitingList==0 and self.waitingListTickets==0 and self.totalRac==0:
            print("No Tickets Available")
            return 
        passengerName=input("Enter Passenger Name: ")
        passengerAge=int(input("Enter Passenger age: "))
        passengerGender=input("Enter Passenger Gender(M/F): ").upper()
        berthPreference=input("Enter Berth Preference (Lower/Middle/Upper): ").lower()

        if passengerAge<5:
            print("Under aged. Not allowed to book Ticket")
            return 
        foundTicket=1
        if berthPreference=='lower':
            if self.lowerBerth>0:
                self.lowerBerth-=1
                self.totalBerth-=1
            else:
                print(f'{berthPreference}Berth not Available')
                suggested=rtrs.suggestion()
                foundTicket=0
        elif berthPreference=='middle':
            if self.middleBerth>0:
                self.middleBerth-=1
                self.totalBerth-=1
            else:
                print(f'{berthPreference}Berth not Available')
                suggested=rtrs.suggestion()
                foundTicket=0
        elif berthPreference=='upper':
            if self.upperBerth>0:
                self.upperBerth-=1
                self.totalBerth-=1
            else:
                print(f'{berthPreference}Berth not Available')
                suggested=rtrs.suggestion()
                foundTicket=0
        else:
            print("Invalid Choice")
            return
        
        if foundTicket == 0:
            if suggested is None:
                print("No Tickets Available")
                return
            else:
                choice = input(f'{suggested} is available, is it ok?(y/n): ').lower()
                if choice == 'y':
                    if suggested == "Rac":
                        self.RACTickets.append(Passenger(passengerName, passengerAge, passengerGender, suggested))
                        self.totalRac -= 1
                    elif suggested == "waiting":
                        self.waitingListTickets.append(Passenger(passengerName, passengerAge, passengerGender, suggested))
                        self.totalWaitingList -= 1
                    else:
                        rtrs.bookedTickets.append(Passenger(passengerName, passengerAge, passengerGender, suggested))
                        if suggested == "lower":
                            self.lowerBerth -= 1
                        elif suggested == "middle":
                            self.middleBerth -= 1
                        elif suggested == "upper":
                            self.upperBerth -= 1
                    print(f"Ticket booked under {suggested} category!")
                else:
                    print("Thank you for checking.")
                    return

        else:
            rtrs.bookedTickets.append(Passenger(passengerName,passengerAge,passengerGender,berthPreference))
            self.totalBerth-=1

rtrs=rtrs()    
while True:
    print("Railway Ticket Reservation System")
    print("1. Book Ticket")
    print("2. Cancel Ticket")
    print("3. Print  Booked Ticket")
    print("4. Print Available Ticket")
    print("5. Exit")

    choice=int(input("Enter Your Choice: "))

    if choice==1:
        rtrs.bookTicket()
    elif choice==2:
        rtrs.cancelTicket()
    elif choice==3:
        rtrs.printBookedTicket()
    elif choice==4:
        rtrs.printAvailableTicket()
    elif choice==5:
        exit()
    else:
        print("Invalid Choice")
    print()

