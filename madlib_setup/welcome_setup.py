from sys import exit
from madlib_setup.welcome_text import welcome

game_options = {
  '1': {
      'title': 'A Dark and Stormy Night', 
      'file_path': 'assets/dark_and_stormy_night_template.txt'
      },
  '2': {
      'title': 'Make Me A Video Game!',
      'file_path': 'assets/sample_template.txt'
    },
    '3': {
        'title': 'Space Cats',
        'file_path': 'assets/space_cats.txt'
    }
}

def welcome_setup():
    print(welcome)
    for key in game_options:
        print(f'press {key}: {game_options[key]["title"]}')
    print('\nq or quit to exit')
    choice = input('Which story would you like to create?  > ')
    if (choice.lower() == 'q') | (choice.lower() == 'quit'):
        exit()
    else:
        print(f'You have chosen {game_options[choice]["title"]}')
    return game_options[choice]
