#!/usr/bin/env python3

def greetings(text = None):
    if not text:
        print('Hello, noble stranger.')
    else:
        try:
            int(text)
            print('Error! It was not a name.')
        except:
            print(f'Hello, {text}.')

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
