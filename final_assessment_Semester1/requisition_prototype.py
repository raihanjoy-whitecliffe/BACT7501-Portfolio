counter = 10000  # Counter to create req id

class Requisition:
    total_submitted = 0  # To increment after each requisition submitted for statistics
    total_pending = 0  # to increment or decrement based on requirement for statistics
    total_approved = 0  # to increment or decrement based on requirement for statistics
    total_not_approved = 0  # for statistics

    def __init__(self):
        global counter  # this counter will be used to generate approval id
        # initializing the shared data which were previously used
        counter += 1
        self.date = ""
        self.staff_name = ""
        self.staff_id = ""
        self.status = "Pending"
        self.id = counter
        self.total = 0
        self.approval_ref = "N/A"
        # these are incremented so that each time the code starts from the top
        # it takes a requisition and marks it as pending
        Requisition.total_submitted += 1
        Requisition.total_pending += 1

    def add_requisition(self):
        print("-------Submit Requisition-------")

        self.date = input("Enter Submission Date (DD/MM/YYYY): ")
        while self.date.strip() == "": #checking if the field is empty
            print("Date cannot be empty!")
            self.date = input("Enter Submission Date (DD/MM/YYYY): ")


        self.staff_id = input("Enter Staff ID: ")
        while self.staff_id.strip() == "": #checking if the field is empty
            print("Staff ID cannot be empty!")
            self.staff_id = input("Enter Staff ID: ")


        self.staff_name = input("Enter Staff Name: ")
        while self.staff_name.strip() == "": #checking if the field is empty
            print("Staff Name cannot be empty!")
            self.staff_name = input("Enter Staff Name: ")

        print("--------Add Item--------")
        input("Enter Item Name: ")
        price_input = input("Enter Item Price:$")
        while price_input.strip() == "": #checking if the field is empty
            print("Price cannot be empty!")
            price_input = input("Enter Item Price:$")
        item_price = float(price_input)

        self.total += item_price
        more_items = input(
            "Any Other Items You Would Like to Add? (yes/no): :").lower()  # to avoid error if there are capitalization errors
        while more_items == "yes":
            input("Enter Item Name: ")

            price_input = input("Enter Item Price:$")
            while price_input.strip() == "":
                print("Price cannot be empty!")
                price_input = input("Enter Item Price:$")
            item_price = float(price_input)

            self.total += item_price
            more_items = input("Any Other Items You Would Like to Add? (yes/no): :").lower()
        print("Total: $", self.total)

    def approve_requisition(self):
        # Checking if the total is above or below 500
        if self.total < 500:
            self.status = "Approved"
            self.approval_ref = self.staff_id + str(self.id)[-3:]  # generating approval id if the req is approved
            Requisition.total_pending -= 1  # as approved, it is no longer pending
            Requisition.total_approved += 1  # incremented as the req is approved
        else:
            self.status = "Pending"  # if the total is more than 500, it is marked as pending for manager checks

    def manager_approval(self):
        if self.status == "Pending": #all the status with pending is taken in account to check
            print("---------- Statistics before manager response ----------")
            self.requisition_statistics()
            decision = input("Is it approved by a manager? (yes/no): :").lower() #to avoid errors regarding upper/lower case
            if decision == "yes":
                self.status = "Approved"
                self.approval_ref = self.staff_id + str(self.id)[-3:] #reference id is created based on assignment requirements
                Requisition.total_pending -= 1
                Requisition.total_approved += 1
            else:
                self.status = "Not Approved"
                Requisition.total_pending -= 1 #it is no more pending
                Requisition.total_not_approved += 1 #as requisition was not approved
        else:
            print("Decision was already given")

    def display_requisition(self):
        print("---------Displaying Requisition---------")
        print("Date:", self.date)
        print("Requisition ID:", self.id)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)
        print("Total: $", self.total)
        print("Status: ", self.status)
        print("Approval Reference ID:", self.approval_ref)

    def requisition_statistics(self):
        print("Total number of requisitions submitted:", Requisition.total_submitted)
        print("Total number of approved requisitions:", Requisition.total_approved)
        print("Total number of pending requisitions:", Requisition.total_pending)
        print("Total number of not approved requisitions:", Requisition.total_not_approved)


# asking for 5 requisitions
req1 = Requisition()
req1.add_requisition()
req1.approve_requisition()
if req1.status == "Pending":
    req1.manager_approval()

req2 = Requisition()
req2.add_requisition()
req2.approve_requisition()
if req2.status == "Pending":
    req2.manager_approval()

req3 = Requisition()
req3.add_requisition()
req3.approve_requisition()
if req3.status == "Pending":
    req3.manager_approval()

req4 = Requisition()
req4.add_requisition()
req4.approve_requisition()
if req4.status == "Pending":
    req4.manager_approval()

req5 = Requisition()
req5.add_requisition()
req5.approve_requisition()
if req5.status == "Pending":
    req5.manager_approval()

# Printing Final Requisitions
req1.display_requisition()
req2.display_requisition()
req3.display_requisition()
req4.display_requisition()
req5.display_requisition()

# final stats after manager decision
print("---------- Statistics after manager response ----------")
req5.requisition_statistics()