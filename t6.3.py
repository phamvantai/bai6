class Nguoi(object):
    def getGender(self):
        return"Unknown"

class Nam(Nguoi):
    def gerGender(self):
        return"Nam"
#Code by Daihocvinh
class Nu(Nguoi):
    def getGender(self):
        return"Nu"

aNam = Nam()
aNu = Nu()
print(aNam.getGender())
print(aNu.getGender())
