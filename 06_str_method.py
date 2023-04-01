class Person:
    def __init__(self, name, address, email) -> None:
        self.name = name
        self.address = address
        self.email = email
    
    def report(self):
        print("-"*50)
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"email: {self.email}")
        print("-"*50)
    
    def __str__(self) -> str:
        return f"Name: {self.name} Address: {self.address} Email: {self.email}"


csaba = Person("Csaba", "Budapest", "csaba@gmail.com")
kriszta = Person("Kriszta", "Debrecen", "kriszta@gmail.com")
tamas = Person("Tamás", "Pécs", "tamas@gmail.com")

print(csaba)
print(kriszta)
print(tamas)