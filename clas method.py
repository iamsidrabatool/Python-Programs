class Employee:
  company = "Apple"
  id=4
  def show(self):
    print(f"The name is {self.name} and company is {self.company}")

  @classmethod
  def changeCompany(cls, newCompany):
    cls.company = newCompany
  @classmethod
  def changeid(cls, newid):
    cls.id = newid


e1 = Employee()
e1.name = "Harry"
e1.show()
e1.changeCompany("Tesla")
e1.changeid(3)
e1.show()
print(Employee.id)
print(Employee.company)