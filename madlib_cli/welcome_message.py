from sys import exit

welcome = '''
    WElcome to MADLIBS!


Get ready to play Madlibs! The funniest game ever made! 
Fill in the words that are prompted and then die from laughter!
When you finish choosing your words the story will print and you'll laugh milk from your nose.
It will obviously be the funniest thing you have ever done in your whole life! 
Pick a story to laugh until your pants are wet!
'''

game_options = {
  '1': {
      'title': 'A Dark and Stormy Night', 
      'file_path': 'assets/dark_and_stormy_night_template.txt'
      },
  '2': {
      'title': 'Make Me A Video Game!',
      'file_path': 'assets/sample_template.txt'
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
