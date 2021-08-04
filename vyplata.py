class Employee:
  def get_net_salary(self):
      tax = self.gross_salary * 0.15 - self.children * 1500
      return self.gross_salary - tax
  def get_info(self):
    return f"{self.name} pracuje na pozici {self.position}."
  def __init__(self, name, position, gross_salary, children):
    self.name = name
    self.position = position
    self.gross_salary = gross_salary
    self.children = children
zam1 = Employee("František Novák", "konstruktér", 45000, 2)
print(zam1.get_net_salary())
