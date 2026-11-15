class Member:
    def __init__(self, name, visits, months, monthly_fee):
        self.name = name
        self.visits = visits
        self.months = months
        self.monthly_fee = monthly_fee

    def is_at_risk(self):
        return self.visits < 4 and self.months > 6 
    def total_paid(self):
        return self.months * self.monthly_fee
m1 = Member("patithan khanbualom", 2, 10, 900)
m2 = Member("john doe", 5, 12, 900)
m3 = Member("jane smith", 1, 8, 900) 
m4 = Member("alice johnson", 3, 7, 900)   
print("ชื่อสมาชิก;", m1.name)
print("เสี่ยงเลิกใช้บริการ;", m1.is_at_risk())
print("ชื่อสมาชิก;", m2.name)
print("เสี่ยงเลิกใช้บริการ;", m2.is_at_risk())
print("ชื่อสมาชิก;", m3.name)
print("เสี่ยงเลิกใช้บริการ;", m3.is_at_risk())
print("ชื่อสมาชิก;", m4.name)
print("เสี่ยงเลิกใช้บริการ;", m4.is_at_risk())
print("ยอดชำระรวม;", m1.total_paid(), "บาท")
print("ยอดชำระรวม;", m2.total_paid(), "บาท")
print("ยอดชำระรวม;", m3.total_paid(), "บาท")
print("ยอดชำระรวม;", m4.total_paid(), "บาท")
