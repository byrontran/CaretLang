import procedures, utils

def interpret(tokens, program_state):

  # print(f"Evaluating: {tokens}") # debug line

  if isinstance(tokens, utils.Identifier):

    result = program_state.locate(tokens)[tokens]
    return result
  
  elif not isinstance(tokens, utils.List):
    return tokens
  
  elif tokens[0] == "program-start":
    for expression in tokens[1:]:
      result = interpret(expression, program_state)
      if result:
        print(result)

    return result 

  elif tokens[0] == "def":
    (procedure, identifier, body) = tokens
    program_state[identifier] = interpret(body, program_state)
    # note: this leaves room for users to overwrite procedure functionality
    #  - if procedure is being run or is in scope and the definition changes, could
    #    lead to unexpected behavior?? to be explored at a later time if wanted

  elif tokens[0] == "lambda":
    (procedure, parameters, body) = tokens
    return procedures.Procedure(parameters, body, program_state)
  
  elif tokens[0] == "if":
    (procedure, condition, ifbranch, elsebranch) = tokens
    # evaluate the condition with the program state in mind
    if interpret(condition, program_state):
      result = ifbranch
    else:
      result = elsebranch
    return interpret(result, program_state)
  
  else:
    # base case of the recursive interpreter
    procedure = interpret(tokens[0], program_state)

    parameters = []
    for expr in tokens[1:]:
      parameters.append(interpret(expr, program_state))

    return procedure(*parameters)
