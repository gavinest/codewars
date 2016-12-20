'''
Complete the function/method so that it takes CamelCase string and returns the string in snake_case notation. Lowercase characters can be numbers. If method gets number, it should return string.


Note: upon submitting solutions I realized this can be done much simplier with regular expressions.
'''


def to_underscore(string):
    if str(string).isdigit():
        return str(string)
    else:
      idxs = [i for i, l  in enumerate(string) if l.isupper()]
      l = []
      for i, v in enumerate(idxs[1:]):
          l.append(string[idxs[i]:v])
      l.append(string[idxs[-1]:])
      return '_'.join(l).lower()

if __name__ == '__main__':
    string = 'TestControllerDevice'
    print to_underscore(string)
