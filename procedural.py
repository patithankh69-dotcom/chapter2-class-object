name="patithan khanbualom"
visits=2
months=10

def is_at_risk(visits, months):
    return visits < 4 and months > 6

print("ชื่อสมาชิก;", name)
print("จำนวนครั้งที่ใช้งาน;", visits)
print("อายุสมาชิก;", months ,"เดือน")
print("เสี่ยงเลิกใช้บริการ;", is_at_risk(visits, months))

