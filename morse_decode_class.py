import json
import re

class Morse:
  """
    Morse decoder.
  """

  def __init__(self, decode_dict_path = './dict/dict_en_decode.json'):
    """
        Construct a new 'Morse' object.
        :param decode_dict_path - dictionary to decode message from Morse code
    """
    with open(decode_dict_path, 'r') as json_file:
      self.morse_decode_dict = json.load(json_file)

  def decode(self, text):
    """
    Decode message from Morse code
    :param text - Morse code encrypted message
    """
    text = text.lower().strip()
    text_by_words = text.split('   ')
    message = ''
    for word in text_by_words:
      message += self.decode_word(word) + ' '
    return message.lstrip()

  def decode_word(self, text):
    """
      Decode word from Morse code
      :param text - Morse code encrypted word
    """
    alp = text.split(' ')
    word = ''
    for a in alp:
      word += self.morse_decode_dict.get(a)
    return word

if __name__ == "__main__":
  path = './dict/dict_en_decode.json'
  # message = '.... . -.--   .--- ..- -.. .'
  # message = '... --- ...'
  morse_decoder = Morse(path)
  print('input: ')
  message = input() 
  print(morse_decoder.decode(message))
