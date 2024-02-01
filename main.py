import pycodestyle
import pprint

BAD_PYTHON = '''foo=42
bar ='ham'
meh=[1,2,3,4]
def blah():
    print(5)
def blo():
    print(6)
'''

class HackedReport(pycodestyle.BaseReport):
    '''
    Der Report muss immer gepflegt sein!
    '''

    def __init__(self, *args, **kwargs):
        '''create my own messages!'''
        super().__init__(*args, **kwargs)
        self.messages = []

    def error(self, line_number, offset, text, check):
        '''stfu, just collect my fails'''
        err_d = {
            'line_number': line_number,
            'offset': offset,
            'text': text,
            'check': check.__name__,
        }
        self.messages.append(err_d)


styleguide = pycodestyle.StyleGuide(reporter=HackedReport)
styleguide.input_file(filename='bad code', lines=BAD_PYTHON.split('\n'))
pprint.pprint(styleguide.options.report.messages)
