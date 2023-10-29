class Tenant:
    def __init__(self, name, contact, lease_start_date, apartment, rent):
        self.name = name
        self.contact = contact
        self.lease_start_date = lease_start_date
        self.apartment = apartment
        self.rent = rent

    def update_contact(self, new_contact):
        self.contact = new_contact

    def display_info(self):
        return f"Tenant Name: {self.name}\nContact: {self.contact}\nLease Start Date: {self.lease_start_date}\nApartment: {self.apartment}\nRent: {self.rent}"

class Rent:
    def __init__(self, amount, due_date):
        self.amount = amount
        self.due_date = due_date
        self.is_paid = False

    def record_payment(self):
        self.is_paid = True

    def check_payment_status(self):
        return "Paid" if self.is_paid else "Overdue"

class Apartment:
    def __init__(self, apartment_number, square_footage, rent_amount):
        self.apartment_number = apartment_number
        self.square_footage = square_footage
        self.rent = Rent(rent_amount, "1st of the month")

    def display_details(self):
        return f"Apartment Number: {self.apartment_number}\nSquare Footage: {self.square_footage}\nRent: ${self.rent.amount} (Due {self.rent.due_date})"

class TenantInformation:
    def __init__(self):
        self.tenants = []
        self.apartments = []

    def add_tenant(self, tenant):
        self.tenants.append(tenant)
        self.apartments.append(tenant.apartment)

    def update_lease_history(self, tenant, apartment):
        tenant_info = [t for t in self.tenants if t == tenant]
        apartment_info = [a for a in self.apartments if a == apartment]
        if tenant_info and apartment_info:
            tenant_info[0].lease_start_date = apartment_info[0].rent.due_date

    def find_tenant_info(self, tenant_name):
        for tenant in self.tenants:
            if tenant.name == tenant_name:
                return tenant.display_info()
        return "Tenant not found."

class Policy:
    def __init__(self, policy_id, description, effective_date):
        self.policy_id = policy_id
        self.description = description
        self.effective_date = effective_date

    def check_compliance(self):
        return "Compliant"  # Implement policy compliance checks as needed

class MaintenanceRequest:
    def __init__(self, request_id, description, status, date_reported):
        self.request_id = request_id
        self.description = description
        self.status = status
        self.date_reported = date_reported

    def update_status(self, new_status):
        self.status = new_status

class BuildingManagementSystem:
    def __init__(self):
        self.tenant_information = TenantInformation()
        self.maintenance_requests = []

    def list_overdue_tenants(self):
        overdue_tenants = [tenant for tenant in self.tenant_information.tenants if not tenant.rent.is_paid]
        return [tenant.name for tenant in overdue_tenants]

    def add_maintenance_request(self, request):
        self.maintenance_requests.append(request)

    def list_open_maintenance_requests(self):
        open_requests = [request for request in self.maintenance_requests if request.status == "Open"]
        return open_requests

# Example usage of the building management system
bms = BuildingManagementSystem()

apartment101 = Apartment("101", 900, 1200)
apartment102 = Apartment("102", 1000, 1300)

tenant1 = Tenant("Kiril Iliev", "Kireto@email.com", "2023-01-01", apartment101, Rent(1200, "1st of the month"))
tenant2 = Tenant("Alina Popova", "Alinka@email.com", "2023-02-15", apartment102, Rent(1300, "1st of the month"))

bms.tenant_information.add_tenant(tenant1)
bms.tenant_information.add_tenant(tenant2)
bms.tenant_information.update_lease_history(tenant1, apartment101)
bms.tenant_information.update_lease_history(tenant2, apartment102)

# The rest of the code remains the same

policy1 = Policy(1, "No pets allowed", "2023-01-01")
policy2 = Policy(2, "Quiet hours after 22:00", "2023-02-01")

maintenance_request1 = MaintenanceRequest(1, "Leaky faucet", "Open", "2023-03-10")
maintenance_request2 = MaintenanceRequest(2, "Broken window", "Closed", "2023-03-15")

bms.add_maintenance_request(maintenance_request1)
bms.add_maintenance_request(maintenance_request2)

print("Overdue Tenants:", bms.list_overdue_tenants())
print("\nTenant Information:")
print(bms.tenant_information.find_tenant_info("Alina Popova"))
print(bms.tenant_information.find_tenant_info("Kiril Iliev"))
print("\nApartment Details:")
print(apartment101.display_details())
print(apartment102.display_details())
print("\nPolicies:")
print(policy1.description)
print(policy2.description)
print("\nOpen Maintenance Requests:")
for request in bms.list_open_maintenance_requests():
    print(request.description)