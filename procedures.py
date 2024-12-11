import math, operator
import interpreter, state, utils

class Procedure(object):
  "TODO: support user-defined procedures"
  def __init__(self, parameters, body, state):
    self.parameters = parameters
    self.body = body
    self.state = state

  def __call__(self, *args):
    return interpreter.interpret(self.body, state.State(self.parameters, args, self.state))

def standard_procedures():
  return {
    'program-start': lambda *expr: expr[-1],
    'list': lambda *items: list(items),
    'first': lambda list: list[0],
    'rest': lambda list: list[1:],
    'construct': lambda first, rest: [first] + rest,

    'print': print,
    'length': len,
  
    '+':operator.add,
    '-':operator.sub,
    '*':operator.mul,
    '/':operator.truediv, 
    '=':operator.eq,
    '>':operator.gt,
    '<':operator.lt,
    '>=':operator.ge,
    '<=':operator.le,
    'not':operator.not_,

    'floor':math.floor,
    'ceiling':math.ceil,
    'modulo':operator.mod,
    'abs':abs,
    'round':round,

    'equal?': operator.eq,
    'null?': lambda x: x == [],
    'number?': lambda x: isinstance(x, utils.Number),
    'identifier?': lambda x: isinstance(x, utils.Identifier),
    'procedure?': callable,
  }
