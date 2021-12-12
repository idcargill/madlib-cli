import re
from madlib_setup.welcome_setup import welcome_setup

def read_template(file_path):
  '''
  returns text file content
  '''
  with open(file_path, 'r') as reader:
    file_text = reader.read()
    return file_text

def parse_template(text):
  '''
  returns a tuple of texts to prompt for user input
  returns a text template string
  '''
  regex_test = r"{([\w ',.-]+)}"
  prompts = tuple(re.findall(regex_test, text))
  text_template = re.sub(regex_test, '{}', text)
  return text_template, prompts
  
def merge(text_template, user_submissions):
  '''
  string format: adds user submissions to the template string
  '''
  return text_template.format(*user_submissions)

def handle_input(arr):
  '''
  collect user input given an array of word prompts
  '''
  user_answers = []
  for i in arr:
    user_input = input(f'Choose next word: {i} -->')
    user_answers.append(user_input)
  return user_answers

def save_to_file(story, title):
  '''
  save passed in story text to a file with given title.
  '''
  with open(f'saved_madlibs/{title}.txt', 'w') as writable:
    writable.write(story)

def madlib_controller(file):
  '''
  Takes in an object of file template location and game title.
  Collects user input based on word descriptor prompts.
  Mergest user input words with story template and returns the completed madlib.
  Writes the most recent file to a saved_madlibs directory. 
  '''
  text = read_template(file['file_path'])
  text_template, prompts = parse_template(text)
  user_answers = handle_input(prompts)
  final_madlib = merge(text_template, user_answers)
  save_to_file(final_madlib, file['title'])
  print(final_madlib)



## Main File Execution
if __name__ == '__main__':
  game = welcome_setup()
  madlib_controller(game)

