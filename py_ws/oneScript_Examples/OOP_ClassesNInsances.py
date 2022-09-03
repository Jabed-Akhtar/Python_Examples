"""
 ******************************************************************************
 * @author     : Jabed-Akhtar (github)
 * @Created on : 03.09.2022
 ******************************************************************************
 * @file       : OOP_ClassesNInsances.py
 * @brief      : ---
 ******************************************************************************
 * :Descriptions/Infos:
 *      - ---
 ******************************************************************************
"""


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Ja', 'Akh', 5000)
emp_2 = Employee('Sa', 'Haq', 2000)

print(emp_2.fullname()) # we need bracket here, because it's method and not an attribute
print(emp_2.email)

# The below both are the same!
print(emp_1.fullname())
print(Employee.fullname(emp_1))

if __file__ == "__main__":
    pass


# ****************************** END OF FILE **********************************