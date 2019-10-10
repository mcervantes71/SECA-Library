import aiml
from SECA import *

print("everything start here :D")

my_seca = SECA(1, "Happy",["happy","neutral","sad"], ["smile","neutral", "cry"])




kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")


while True:
    print kernel.respond(raw_input("Enter your message >> "))