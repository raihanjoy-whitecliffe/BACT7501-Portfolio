# class with method for storing employee info
class TicketInfo:
    def __init__(self, id, date, emp_id, name, description, priority, status, resolution):
        self.id = id
        self.date = date
        self.emp_id = emp_id
        self.name = name
        self.description = description
        self.priority = priority
        self.status = status
        self.resolution = resolution


class HelpDeskManagement:
    # initialized data for incrementing and updating
    def __init__(self):
        self.tickets = []
        self.id = 10101
        self.submitted = 0
        self.resolved = 0
        self.in_progress = 0
        self.closed = 0

    # Creating and submitting ticket
    def submit_ticket(self):
        print("-------Submit New Ticket-------")
        date = input("Enter Submission Date (DD/MM/YYYY): ")
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        description = input("Enter Issue Description: ")
        # conditions for checking priority and providing status
        if description == "Password Reset":
            priority = "Low"
            status = "Resolved"
            password = emp_id[:2] + name
            resolution = "Auto-resolved with instructions sent. Temp Password: " + password
            self.resolved += 1
        elif description == "System Outage":
            priority = "High"
            status = "In Progress"
            resolution = "Pending Manager Approval"
            self.in_progress += 1
        else:
            priority = "Low"
            status = "In Progress"
            resolution = "N/A"
            self.in_progress += 1

        new_ticket = TicketInfo(self.id, date, emp_id, name, description, priority, status, resolution)
        self.tickets.append(new_ticket)
        self.id += 1
        self.submitted += 1

    def show_all_tickets(self):
        print("------Printing Tickets------")
        for t in self.tickets:
            print("Date:", t.date)
            print("Ticket ID:", t.id)
            print("Employee ID:", t.emp_id)
            print("Employee Name:", t.name)
            print("Issue Description:", t.description)
            print("Priority:", t.priority)
            print("Status:", t.status)
            print("Resolution Message:", t.resolution)
            print()

    def display_statistics(self):
        print("------Statistics------")
        print("Total number of tickets submitted:", self.submitted)
        print("Total number of resolved tickets:", self.resolved)
        print("Total number of tickets in progress:", self.in_progress)
        print("Total number of closed tickets:", self.closed)


test = HelpDeskManagement()
# 2 objects:
test.submit_ticket()
test.submit_ticket()
# prints ticket and statistics
test.show_all_tickets()
test.display_statistics()