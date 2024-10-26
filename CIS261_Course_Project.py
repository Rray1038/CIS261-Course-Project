#Raymond Ray
#CIS261
#Course Project
def tax_and_netpay_calculation(total_hours, hourly_rate, tax_rate):
    tax = float(total_hours) * float(hourly_rate) * (float(tax_rate) / 100)
    net_pay = float(total_hours) * float(hourly_rate) - tax
    return tax, net_pay

def get_employee_name():
    employee_name = input("Enter the employee's name: ")
    return employee_name

def get_total_hours():
    total_hours = float(input("Enter the total hours worked: "))
    return total_hours

def get_hourly_rate():
    hourly_rate = float(input("Enter the hourly rate associated with the employee: "))
    return hourly_rate

def get_tax_rate():
    tax_rate = float(input("Enter the tax rate associated with the employee: "))
    return tax_rate

def get_gross_pay(total_hours, hourly_rate):
    gross_pay = float(total_hours) * float(hourly_rate)
    return gross_pay

def employee_displayed_info(employee_name, total_hours, hourly_rate, tax_rate, tax, gross_pay, net_pay):
    print("-" * 20)
    print("Employee Name: ", employee_name)
    print("Total Hours Worked: ", total_hours)
    print("Associated Hourly Rate: ", hourly_rate)
    print("Associated Tax Rate: ", tax_rate)
    print("Gross Pay: ", gross_pay)
    print("Income Tax: ", tax)
    print("Net Pay: ", net_pay)
    print("-" * 20)
    
def total_displayed_info(total_employees, total_hours, total_tax, total_gross_pay, total_net_pay):
    print("-" * 20)
    print("Total Number of Employees Within Database: ", total_employees)
    print("Total Amount of Hours Worked: ", total_hours)
    print("Total Amount of Tax: ", total_tax)
    print("Total Gross Pay Accumulated: ", total_gross_pay)
    print("Total Net Pay Accumulated: ", total_net_pay)
    print("-" * 20)
    
def main():
    total_employees = 0
    total_hours = 0
    total_tax = 0
    total_gross_pay = 0
    total_net_pay = 0
        
    while True:
        name = get_employee_name()
        if name == "End":
            break
        hours = get_total_hours()
        hourly_rate = get_hourly_rate()
        tax_rate = get_tax_rate()
        gross_pay = get_gross_pay(hours, hourly_rate)
        tax, net_pay = tax_and_netpay_calculation(hours, hourly_rate, tax_rate)
        employee_displayed_info(name, hours, hourly_rate, tax_rate, tax, gross_pay, net_pay)
            

        total_employees += 1
        total_hours += hours
        total_tax += tax
        total_gross_pay += gross_pay
        total_net_pay += net_pay
        
    total_displayed_info(total_employees, total_hours, total_tax, total_gross_pay, total_net_pay)
        

if __name__ == "__main__":
    main() 