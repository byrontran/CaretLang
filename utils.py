Identifier = str
# Character = str
List = list
Number = (int, float)

def Atom(token):

  try:
    token = int(token)
    return token
  except:
    try: 
      token = float(token)
      return float(token)
    except:
      try:
        return Identifier(token)
      except:
        print(f"Token is of unrecognized type: {token}")


