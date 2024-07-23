import sys
import os


class things:
    name = None
    num = None


class Stu(things):
    pass


class Tea(things):
    pass


class Sch(things):
    pass


class make:
    cho = None

    def getClass(self, cho=None):
        self.cho = cho
        if self.cho is None:
            return Stu()
        if self.cho == "Stu":
            return Stu()
        if self.cho == "Tea":
            return Tea()
        if self.cho == "Sch":
            return Sch()
