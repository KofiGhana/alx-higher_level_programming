#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("Abraham", "Karikari")
say_my_name("Nana", "Kofi")
say_my_name("Maximus")
try:
    say_my_name(12, "Kofi")
except Exception as e:
    print(e)
