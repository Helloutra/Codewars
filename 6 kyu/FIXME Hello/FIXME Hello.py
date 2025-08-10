class Dinglemouse(object):

    def __init__(self):
        self._order = []
        self.age = None
        self.name = None
        self.sex = None

    def setAge(self, age):
        self.age = age
        if 'age' not in self._order:
            self._order.append('age')
        return self

    def setName(self, name):
        self.name = name
        if 'name' not in self._order:
            self._order.append('name')
        return self

    def setSex(self, sex):
        self.sex = sex
        if 'sex' not in self._order:
            self._order.append('sex')
        return self

    def hello(self):
        result = []
        for attr in self._order:
            value = getattr(self, attr)
            if value is not None and value != "":
                if attr == 'name':
                    result.append(f"My name is {value}.")
                elif attr == 'sex':
                    if value == 'M':
                        result.append("I am male.")
                    elif value == 'F':
                        result.append("I am female.")
                elif attr == 'age':
                    result.append(f"I am {value}.")
        return "Hello." + (" " + " ".join(result) if result else "")