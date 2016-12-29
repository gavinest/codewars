'''
This kata requires you to write an object that receives a file path and does operations on it. NOTE FOR PYTHON USERS: You cannot use modules os.path, glob, and re

The purpose of this kata is to use string parsing, so you're not supposed to import external libraries. I could only enforce this in python.

Try out my new kata here and here

Example of how the tests would work:

Python:

>>> master = FileMaster('/Users/person1/Pictures/house.png')
>>> master.extension()
'png'
>>> master.filename()
'house'
>>> master.dirpath()
'/Users/person1/Pictures/'
'''

class FileMaster():
    def __init__(self, filepath):
        self.fp = filepath.split('/')
    def extension(self):
        return self.fp[-1].split('.')[1]
    def filename(self):
        return self.fp[-1].split('.')[0]
    def dirpath(self):
        return '/'.join(self.fp[:-1]) + '/'

if __name__ == '__main__':
    master = FileMaster('/Users/person1/Pictures/house.png')
    print master.extension()
    print master.filename()
    print master.dirpath()
