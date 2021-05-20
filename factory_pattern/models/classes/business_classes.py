from ..base.base import BaseRunnable

class ARunnable(BaseRunnable):

    def __init__(self, name='', age=0):
        self.name = name
        self.age = age

    def run(self):
        print(f"Running {self.__class__.__name__} with {','.join(self.__dict__.keys())} properties")


class BRunnable(BaseRunnable):

    def __init__(self, name='', height=0):
        self.name = name
        self.height = height

    def run(self):
        print(f"Running {self.__class__.__name__} with {','.join(self.__dict__.keys())} properties")


class CRunnable(BaseRunnable):

    def __init__(self, name='', age=0, expertise=''):
        self.name = name
        self.age = age
        self.expertise = expertise

    def run(self):
        print(f"Running {self.__class__.__name__} with {','.join(self.__dict__.keys())} properties")


class DRunnable(BaseRunnable):

    def __init__(self, name=''):
        self.name = name

    def run(self):
        print(f"Running {self.__class__.__name__} with {','.join(self.__dict__.keys())} properties")


