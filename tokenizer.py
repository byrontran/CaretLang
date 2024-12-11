import sys
from utils import Atom

tokenized = False

def preprocess(source_code):
  """
  Caret uses my variation on LISP as in intermediate language. 
  Needs to be translated before syntactic analysis can begin properly.
  
  My idea with Caret is to make the syntax more approachable than LISP,
  although the function bodies are still parentheses-heavy due to
  time constraints.
  """
  # print(source_code)

  code = "(program-start\n" + source_code + "\n)"
  code = code.replace("{", "(").replace("}", ")")
  code = code.replace("def", "(def").replace(";", ")")
  code = code.replace("lambda", "lambda(").replace(":", ")").replace(",", " ")

  lines = code.split("\n")
  for i, line in enumerate(lines):
      if line.startswith("print("):
          line = line.replace("print(", "(print ")
          lines[i] = line.replace("))", ")")

      if line.startswith("print-result"):
          line = line.replace("print-result", "print")
          lines[i] = "(" + line

      if line.startswith("list"):
          lines[i] = "(" + line.strip() + ")"

  intermediate_code = "\n".join(lines)

  # print(intermediate_code)

  return intermediate_code

def tokenize(source_code):
  """
  LISP Tokenizers are super simple due to shear amt of parentheses in source code.
  
  Add whitespace padding to the parentheses, then split based on whitespace to tokenize.
  """
  source_code = source_code.replace("(", " ( ")
  source_code = source_code.replace(")", " ) ")
  tokens = source_code.split()
  return tokens

def parse(tokens):
  """
  Tokenizer leaves parentheses in tokenizer to be able to parse out expressions 
  for syntactic analysis.
  """

  if not tokens:
    print("Error: Parser expecting tokens but none recieved.\n")
    sys.exit(1)
  
  token = tokens.pop(0)

  if token == "(":
    expressions = []
    while tokens[0] != ")":
      expressions.append(parse(tokens))
    tokens.pop(0)
    return expressions

  elif token == ")":
    print(f"Error: Unexpected ')' discovered with no corresponding '('.\n")
    sys.exit(1)

  else:
    return Atom(token)