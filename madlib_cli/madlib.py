import re
from Madlib_Module.welcome_message import welcome


test_path = 'assets/dark_and_stormy_night_template.txt'
sample_template = 'assets/sample_template.txt'

def read_template(file_path):
  with open(file_path, 'r') as reader:
    contents = reader.read()
    return contents

def parse_template(text):
  fill_in = r"{[\w ',.-]+}"
  prompts = re.findall(fill_in, text)
  text_template = re.sub(fill_in, '{}', text)
  return prompts
  # print(prompts)
  # print(text_template.format('cat', 'hat', 'bat'))
  

def merge():
  print('hi')


text = read_template(test_path)

print(parse_template(text))

print(text)


def take_input(arr):
  user_answers = []
  for i in arr:
    i = i.replace('{', '')
    i = i.replace('}', '')
    if i == 'Adjective':
      user_input = input(f'Next word {i} -->')
      user_answers.append(user_input)
    user_input = input(f'Next word {i} -->')
    user_answers.append(user_input)

  return user_answers


print(take_input(parse_template(text)))