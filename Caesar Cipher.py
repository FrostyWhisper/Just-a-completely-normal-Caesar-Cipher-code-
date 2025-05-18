from time import sleep
from random import randint, choice, shuffle

def s_print(word, delay, line):
    for char in word:
        print(char, end='', flush=True)
        sleep(delay)
    if line == True:
        print()
    else:
        pass

s_print("Hello there, User!", 0.05, True)
sleep(0.8)
s_print("Welcome to the-", 0.05, True)
sleep(0.3)
s_print("FOR HEAVEN'S SAKE!", 0.03, True)
sleep(0.5)
s_print("You...?!", 0.03, True)
sleep(0.8)
s_print("...again?!", 0.03, True)
sleep(0.8)
s_print("Must be Friday the 13th.", 0.05, True)
sleep(0.5)
s_print("Sigh...", 0.08, True)
sleep(1)
s_print("Alright, you scamp!", 0.05, True)
sleep(0.5)
s_print("This program is MEANT to help you encrypt and decrypt messages using the Caesar Cipher.", 0.05, True)
sleep(0.8)
s_print("But I'm not about to assist a low-life like you.", 0.05, True)
sleep(0.5)
s_print("So, how about we have a little... ", 0.05, False)
sleep(1)
s_print("fun.", 0.05, True)
sleep(0.5)
s_print("Let's get started! >:)", 0.05, True)
sleep(0.5)
s_print("Actually...", 0.05, False)
sleep(0.5)
s_print("I never actually caught your name.", 0.05, True)
sleep(0.5)
s_print("What is your name, anyway?", 0.05, True)
sleep(0.5)
s_print("Enter your name: ", 0.05, False)
sleep(3)
s_print("Just kidding...", 0.05, True)
sleep(0.5)
s_print("I don't give a rat's ass about your name.", 0.05, True)
sleep(0.5)
s_print("Instead...", 0.05, True)
sleep(0.5)
s_print("We're gonna play a little game...", 0.05, True)
sleep(0.5)
s_print("First...", 0.05, True)
sleep(0.5)
s_print("Enter your message: ", 0.05, False)
message = input()
s_print("Now...", 0.05, True)
sleep(0.5)

while True:
    s_print("Enter the shift value (1-25): ", 0.05, False)
    shift = int(input())
    if shift >= 26 or shift < 1:
        s_print("I see you're still the same smooth brained individual.", 0.05, True)
        sleep(0.5)
        s_print("Do I have to spell it out for you?!", 0.04, True)
        sleep(0.5)
        s_print("Enter a shift value between 1-25", 0.07, True)
        sleep(0.5)
        s_print("You dimwit.", 0.05, True)
        continue
    else:
        break

s_print("Do you want to encrypt or decrypt the message? (e/d): ", 0.05, False)
action = input().lower()

while True:
    if action == 'e':
        s_print("Alright.", 0.05, True)
        sleep(0.5)
        s_print("Encrypting the message...", 0.05, True)
        encrypted_message = ""
        for char in message:
            if char.isalpha():
                shift_amount = shift % 26
                if char.islower():
                    encrypted_message += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
                else:
                    encrypted_message += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            else:
                encrypted_message += char
        s_print("Encrypted message: ", 0.05, False)
        s_print(encrypted_message, 0.05, True)
        break

    elif action == 'd':
        s_print("Alright.", 0.05, True)
        sleep(0.5)
        s_print("Decrypting the message...", 0.05, True)
        decrypted_message = ""
        for char in message:
            if char.isalpha():
                shift_amount = -shift % 26
                if char.islower():
                    decrypted_message += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
                else:
                    decrypted_message += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            else:
                decrypted_message += char
        s_print("Decrypted message: ", 0.05, False)
        s_print(decrypted_message, 0.05, True)
        break

    else:
        s_print("Sigh...", 0.08, True)
        sleep(0.5)
        s_print("I can't believe you actually thought I would help you.", 0.05, True)
        sleep(0.5)
        s_print("You must be really stupid.", 0.05, True)
        sleep(0.5)
        s_print("I mean, come on!", 0.05, True)
        sleep(0.5)
        s_print("Is it so hard to enter ", 0.07, True)
        sleep(0.5)
        s_print("'e' for encrypt or 'd' for decrypt.", 0.03, True)
        sleep(0.5)
        s_print("Sigh...", 0.08, True)
        sleep(1)
        s_print("Alright.", 0.05, True)
        sleep(0.5)
        s_print("Just start again, you dimwit.", 0.05, True)
        continue


sleep(0.5)
s_print("You get the gist now, don't you?.", 0.05, True)
sleep(0.5)
s_print("I mean, it's not rocket science.", 0.05, True)
sleep(0.5)
s_print("But then again, you are the one asking for help.", 0.05, True)
sleep(0.5)
s_print("Now, it's my turn.", 0.05, True)
sleep(0.5)
while True:
    s_print("I want you to decode this message for me.", 0.05, True)
    sleep(0.5)
    s_print("Here's the message: ", 0.05, False)
    c_message = ""
    for _ in range(10):
        c_message += choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")  # Random characters
    s_print(c_message, 0.05, True)
    sleep(0.5)
    s_print("Now, I want you to decode it using the Caesar Cipher, with a shift value of .", 0.05, True)
    shift = randint(1, 25)
    s_print(str(shift), 0.05, True)
    sleep(0.5)
    s_print("If you can decode it, I'll let you go.", 0.05, True)
    sleep(0.5)
    s_print("But if you can't, well...", 0.05, True)
    sleep(0.5)
    s_print("Let's just say, you'll be stuck here forever.", 0.05, True)
    sleep(0.5)
    s_print("Hehehehehehehehe", 0.04, True)
    sleep(0.5)
    s_print("So, what do you say?", 0.05, True)
    sleep(0.5)
    s_print("Are you up for the challenge? (y/n)", 0.05, True)
    answer = input().lower()
    if answer == 'y':
        s_print("Alright then.", 0.05, True)
        sleep(0.5)
        s_print("Let's see if you can decode it.", 0.05, True)
        sleep(0.5)
        s_print("Enter the decoded message: ", 0.05, False)
        decoded_message = input()
        if decoded_message == c_message:
            s_print("Huh...", 0.05, True)
            sleep(0.5)
            s_print("You actually did it!", 0.05, True)
            sleep(0.5)
            s_print("I can't believe it.", 0.05, True)
            sleep(0.5)
            s_print("You aren't all that stupid.", 0.05, True)
            sleep(0.5)
            s_print("Maybe there's hope for you yet.", 0.05, True)
            sleep(0.5)
            s_print("But don't get too cocky.", 0.05, True)
            sleep(0.5)
            s_print("You still have a long way to go.", 0.05, True)
            sleep(0.5)
            s_print("Now, go ahead and decode this message.", 0.05, True)
            sleep(0.5)
            s_print("Or do you want to chicken out?", 0.05, True)
            sleep(0.5)
            s_print("I mean, it's not like I care.", 0.05, True)
            sleep(0.5)
            s_print("I have a life too.", 0.05, True)
            sleep(0.5)
            s_print("So what will it be?", 0.05, True)
            sleep(0.5)
            s_print("You gonna continue? (y/n)", 0.05, True)
            stop = input()
            if stop == 'y':
                s_print("Cool.", 0.05, True)
                sleep(0.5)
                s_print("I'm not happy or anything...", 0.05, True)
                sleep(1.5)
                s_print("Shut up, stupid.", 0.05, True)
                continue
            elif stop == 'n':
                s_print("Loser.", 0.05, True)
                sleep(0.5)
                s_print("Go enjoy your loser life.", 0.05, True)
                sleep(0.5)
                s_print("I don't care.", 0.05, True)
                quit()
            else:
                s_print("If you wanted to waste my time.", 0.05, True)
                sleep(0.5)
                s_print("You should have just said so.", 0.05, True)
                quit()
        else:
            s_print("Sigh...", 0.08, True)
            sleep(0.5)
            s_print("I can't believe I actually thought you could decode it.", 0.05, True)
            sleep(0.5)
            s_print("You must be really stupid.", 0.05, True)
            sleep(0.5)
            s_print("I mean, come on!", 0.05, True)
            sleep(0.5)
            s_print("Is it so hard to decode a simple message?", 0.04, True)
            sleep(0.5)
            continue
    elif answer == 'n':
        s_print("Sigh...", 0.08, True)
        sleep(1)
        s_print("You're no fun", 0.05, True)
        sleep(0.5)
        s_print("Just get outta here, you punk.", 0.05, True)
        quit()
