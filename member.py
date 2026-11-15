class Member:
    def __init__(self, name, visits, months):
        self.name = name
        self.visits = visits
        self.months = months
    def is_at_risk(self):
        return self.visits < 4 and self.months > 6 
    
m1 = Member("patithan khanbualom", 2, 10)
m2 = Member("john doe", 5, 12)
m3 = Member("jane smith", 1, 8)    
print("ชื่อสมาชิก;", m1.name)
print("เสี่ยงเลิกใช้บริการ;", m1.is_at_risk())
print("ชื่อสมาชิก;", m2.name)
print("เสี่ยงเลิกใช้บริการ;", m2.is_at_risk())
print("ชื่อสมาชิก;", m3.name)
print("เสี่ยงเลิกใช้บริการ;", m3.is_at_risk())
       