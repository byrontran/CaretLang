import sys
import tokenizer, interpreter, state

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print(f"Incorrect Number of Arguments. Correct Usage: /'python caret.py <filename>/'")
    sys.exit(1)
  
  file = open(sys.argv[1]);
  source_code = file.read();
  
  intermediate_code = tokenizer.preprocess(source_code)
  tokens = tokenizer.tokenize(intermediate_code)
  abstract_syntax_tree = tokenizer.parse(tokens)

  program_state = state.standard_state()

  interpreter.interpret(abstract_syntax_tree, program_state)


    