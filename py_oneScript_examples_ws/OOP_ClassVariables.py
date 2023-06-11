"""
 ******************************************************************************
 * @author     : Jabed-Akhtar (github)
 * @Created on : 03.09.2022
 ******************************************************************************
 * @file       : OOP_ClassVariables.py
 * @brief      : ---
 ******************************************************************************
 * :Descriptions/Infos:
 *      - ---
 ******************************************************************************
"""


class Employee:

    num_of_emps = 0
    raise_amount = 1.04 # 4%

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1 # this will only for Employee ad´nd not for other instances

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

print(Employee.num_of_emps) # -> 0

emp_1 = Employee('Ja', 'Akh', 5000)
emp_2 = Employee('Sa', 'Haq', 2000)

#print(emp_1.pay)
#emp_1.apply_raise()
#print(emp_1.pay)

print(emp_1.__dict__)
print(Employee.__dict__)

Employee.raise_amount = 1.05 # 5%
emp_1.raise_amount = 1.05 # 5%
print(emp_1.raise_amount)
emp_1.apply_raise() # applying raise to emp_1
print(emp_1.pay)

print(Employee.num_of_emps) # -> 2


if __file__ == "__main__":
    pass


# ****************************** END OF FILE **********************************