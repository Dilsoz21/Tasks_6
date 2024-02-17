#Task_1
#https://edabit.com/challenge/gt9LLufDCMHKMioh2
word =input("Enter the word:")
def stutter(word):
    y = word[0]
    x = word[1]
    print(f"{y}{x}... {y}{x}... {word}")


stutter(word)



#Task_2
#https://edabit.com/challenge/tgEWKRQD8hu5dD3pX
mood = input("enter your mood:")

def default_mood(mood):
    if mood == " ":
        print(f"Today, I am feeling neutral")
    else:
        print(f"Today, I am feeling {mood}")

default_mood(mood)


#Task_3
#https://edabit.com/challenge/p88k8yHRPTMPt4bBo
str = input("enter word: ")

def find_vowels(string):
    result = 0
    vowels = "aouie"
    for alp in string:
        if alp in vowels:
            result += 1

    print(result)


find_vowels(string=str)


#Task_6
string = "the aardvark"

vowel = ["a","e","i","o","u"]
def replace_vowels(string,vowel):
    for x in string:
        if x in vowel:
            string = string.replace(x,"#")
    return string



print(replace_vowels(string,vowel))

#Task_8
#https://edabit.com/challenge/JSJEuuWduBB5hEX6k
input = input("Enter string:")

def task(input):
    x = input.count("x")
    o = input.count("o")
    if x == o:
        print(True)
    elif x <= o or x >= o:
        print(False)
    else:
        print(True)


task(input)

# Task_9
# https://edabit.com/challenge/pKSL3HtApPYAJ72CJ
name = input("Enter the name:")

def name_shuffle(name):
    x = name.split(" ")
    index = x[0]
    index1 = x[1]
    print(f"{index1} {index}")

name_shuffle(name)

# task_10
# https://edabit.com/challenge/nfWirHJzNRBMAp9Df
string = "abcde"
string1 = "abcde"

def uniwue(string, string1):
    i  = 0
    for x in string:
        for y in string1:
            if x==y:
                i+=1
    print(len(string)-i)



uniwue(string, string1)



