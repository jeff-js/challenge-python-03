# Resolve the problem!!
import re

def run():
    encoded_text = ""
    with open('encoded.txt', 'r', encoding='utf-8') as f:
        encoded_text = f.read()
    character_find = re.findall("[a-z]",encoded_text)
    hidden_word = ''.join(character_find)
    print(hidden_word)
    #[ESTE ES EL MENSAJE OCULTO] -> christianvanderhenst

if __name__ == '__main__':
    run()
