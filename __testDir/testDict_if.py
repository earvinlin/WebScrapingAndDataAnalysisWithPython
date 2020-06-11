

choice = 'ham'
print({'spam': 1.25,
       'ham': 1.99,
       'eggs': 0.99,
       'bacon': 1.10}[choice])


"""
# OK, Can run!!
branch = {'spam': 1.25,
          'ham': 1.99,
          'eggs': 0.99}
print(branch.get('spam', 'Bad choice'))
print(branch.get('bacon', 'Bad choice'))
"""