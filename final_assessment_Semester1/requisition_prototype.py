class Requisition:
    counter=10000 #Counter to create req id
    total_submitted=0 #To increment after each requisition submitted for statistics
    total_pending=0 #to increment or decrement based on requirement for statistics
    total_approved=0 #to increment or decrement based on requirement for statistics
    total_not_approved=0 #for statistics
    def __init__(self,date, staff_name, staff_id):
        global counter
        self.date = date
        self.staff_name= staff_name
        self.staff_id= staff_id
        self.status = "Pending"
        self.id= counter
        self.total= 0
        self.approval_reference_ID="N/A"
        Requisition.total_submitted +=1
        Requisition.total_pending +=1
    def add_requisition(self):
        print("-------Submit Requisition-------")
        self.date= input("Enter Submission Date (DD/MM/YYYY): ")
        self.staff_name= input("Enter Staff Name: ")
        self.staff_id= input("Enter Staff ID: ")
        print("--------Add Item--------")
        item_name= input("Enter Item Name: ")
        item_price= input("Enter Item Price:$")
        self.total+=item_price
        more_items= input("Any Other Items You Would Like to Add? (yes/no): :").lower() #to avoid error if there are capitalization errors
        while more_items == "yes":
            item_name= input("Enter Item Name: ")
            item_price= input("Enter Item Price:$")
            self.total+=item_price
            more_items= input("Any Other Items You Would Like to Add? (yes/no): :").lower()
        print("Total: $", self.total)
    def approve_requisition(self):
        if self.total<500:
            self.status="Approved"
            self.approval_reference_ID= self.staff_id + str(self.id)[-3:]
            self.total_pending-=1
            self.total_approved+=1
        else:
            self.status="Pending"