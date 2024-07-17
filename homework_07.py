#problem 0
#1
class Tenant:
    def __init__(self, name, contact_info, lease_start_date):
        self.name = name
        self.contact_info = contact_info
        self.lease_start_date = lease_start_date

    def display_info(self):
        print(f"Tenant Name: {self.name}")
        print(f"Contact Information: {self.contact_info}")
        print(f"Lease Start Date: {self.lease_start_date}")

    def update_contact_info(self, new_contact_info):
        self.contact_info = new_contact_info
        print(f"Contact information updated to: {self.contact_info}")


tenant = Tenant("Julia", "julia@example.com", "2023-05-01")


tenant.display_info()

tenant.update_contact_info("julia.newemail@example.com")

tenant.display_info()

#2
from datetime import date

class Rent:
    def __init__(self, amount, due_date):
        self.amount = amount
        self.due_date = due_date
        self.payment_status = 'overdue' if date.today() > due_date else 'due'
        self.payment_date = None

    def record_payment(self, payment_date):
        self.payment_date = payment_date
        if payment_date <= self.due_date:
            self.payment_status = 'paid'
        else:
            self.payment_status = 'overdue'

    def check_payment_status(self):
        return self.payment_status

    def __str__(self):
        return f'Rent(amount={self.amount}, due_date={self.due_date}, payment_status={self.payment_status}, payment_date={self.payment_date})'

