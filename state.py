import sys
import procedures

def standard_state():
  state = State()
  state.update(procedures.standard_procedures())
  return state

class State(dict):
  def __init__(self, parameters =(), args=(), containing_scope=None):
    self.update(zip(parameters, args))
    self.containing_scope = containing_scope

  def locate(self, var):
    if var in self:
      # print(f"identifier {var} found")
      return self
    
    elif self.containing_scope:
      return self.containing_scope.locate(var)
    else:
      print(f"identifier not found {var}")
      sys.exit(1)
