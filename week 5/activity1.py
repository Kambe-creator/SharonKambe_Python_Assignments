# Parent class
class FaultLine:
    def __init__(self, name, length, type_of_fault, plate_boundary, location):
        self.name = name  # Name of the fault
        self.length = length  # Length in kilometers
        self.type_of_fault = type_of_fault  # e.g., strike-slip, thrust
        self.plate_boundary = plate_boundary  # Associated tectonic boundary
        self.location = location  # Location description

    def describe_fault(self):
        return (f"Fault Name: {self.name}\n"
                f"Length: {self.length} km\n"
                f"Type: {self.type_of_fault}\n"
                f"Plate Boundary: {self.plate_boundary}\n"
                f"Location: {self.location}")

    def earthquake_potential(self):
        return f"The {self.name} has significant earthquake potential due to its plate boundary."

# Child class for the San Andreas Fault
class SanAndreasFault(FaultLine):
    def __init__(self, length, location, slip_rate):
        super().__init__("San Andreas Fault", length, "Strike-Slip", "Transform Boundary", location)
        self.slip_rate = slip_rate  # Slip rate in mm/year

    def earthquake_potential(self):
        # Overrides the parent method with specific details
        return (f"The {self.name} is a major source of seismic activity in California, "
                f"with a slip rate of {self.slip_rate} mm/year.")

# Child class for the Cascadia Fault
class CascadiaFault(FaultLine):
    def __init__(self, length, location, subduction_rate):
        super().__init__("Cascadia Subduction Zone", length, "Thrust", "Convergent Boundary", location)
        self.subduction_rate = subduction_rate  # Subduction rate in mm/year

    def earthquake_potential(self):
        # Overrides the parent method with specific details
        return (f"The {self.name} is capable of producing massive megathrust earthquakes, "
                f"with a subduction rate of {self.subduction_rate} mm/year.")

# Create instances
san_andreas = SanAndreasFault(length=1300, location="California, USA", slip_rate=20)
cascadia = CascadiaFault(length=1000, location="Pacific Northwest, USA & Canada", subduction_rate=40)

# Use methods
print(san_andreas.describe_fault())
print(san_andreas.earthquake_potential())
print("\n")
print(cascadia.describe_fault())
print(cascadia.earthquake_potential())
