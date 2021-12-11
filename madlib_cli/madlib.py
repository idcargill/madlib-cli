import re
from madlib_cli.welcome_message import welcome, welcome_setup

# test_path = 'assets/dark_and_stormy_night_template.txt'
# sample_template = 'assets/sample_template.txt'

def read_template(file_path):
  with open(file_path, 'r') as reader:
    file_text = reader.read()
    return file_text

def parse_template(text):
  regex_test = r"{([\w ',.-]+)}"
  prompts = tuple(re.findall(regex_test, text))
  text_template = re.sub(regex_test, '{}', text)
  return text_template, prompts
  
def merge(text_template, user_submissions):
  return text_template.format(*user_submissions)

def handle_input(arr):
  user_answers = []
  for i in arr:
    user_input = input(f'Choose next word: {i} -->')
    user_answers.append(user_input)
  return user_answers

def save_to_file(story, title):
  with open(f'saved_madlibs/{title}.txt', 'w') as writable:
    writable.write(story)

def madlib_controller(file):
  text = read_template(file['file_path'])
  text_template, prompts = parse_template(text)
  user_answers = handle_input(prompts)
  final_madlib = merge(text_template, user_answers)
  save_to_file(final_madlib, file['title'])
  print(final_madlib)



if __name__ == '__main__':
  game = welcome_setup()
  madlib_controller(game)

