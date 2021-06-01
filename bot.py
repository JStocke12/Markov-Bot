try:
    token = open("token.txt", 'r').read()
except FileNotFoundError:
    raise Exception("No Bot Token: please add the token at token.txt")
