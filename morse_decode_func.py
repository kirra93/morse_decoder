import json
import re

path = './dict/dict_en_decode.json'

morse_decode_dict = {}
with open(path, 'r') as json_file:
  morse_decode_dict = json.load(json_file)


def morse_decode(text):
  text = text.lower().strip()
  text_by_words = text.split('   ')
  message = ''
  for word in text_by_words:
    alp = word.split(' ')
    decoded_word = ''

    for a in alp:
      decoded_word += morse_decode_dict.get(a)

    message += decoded_word + ' '
    
  return message.rstrip()


if __name__ == "__main__":
  print('input: ')
  test_msg = input()
  # test_msg = '- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   .---- ...--   .-.. .- --.. -.--   -.. --- --. ... .-.-.-'

  print(morse_decode(test_msg))