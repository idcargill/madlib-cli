import re
from .welcome_message import welcome

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
  # print(prompts)
  # print(text_template.format('cat', 'hat', 'bat'))
  

def merge():
  print('hi')


text = read_template(test_path)

parse_template(text)


