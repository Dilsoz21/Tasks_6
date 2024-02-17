#task_1
lst =[1, 4, 5, 3, 13, 7]
result = 0

def find(lst, result):
    for x in lst:
        result+=x
    print(result)


find(lst, result)


#Task_2
lst1 = ["d", "a", "x", "o"]
lst2 = []

def add_7(lst1):
    for x in lst1:
        if "7" not in x:
            lst2.append(f"{x}7")
    print((lst2))



add_7(lst1)


#Task_3
num = input("Enter the word:")
lst = ["aeuio"]
result = 0

def find_vowels(num, lst, result):
    for vowel in num:
       for item in lst:
           if vowel in item:
               result += 1
    return result



print(find_vowels(num, lst, result))


#Task_4
def distance():
    string = "abcd"
    string1 ="dboa"
    i = 0
    result = 0
    while len(string)==len(string1):
        x = string[i]
        y = string1[i]

        if x == y:
            result += 1
            print(result)
        i +=1
distance()



#Task_5
txt = "How to ace BC Calculus in 5 Easy Steps"
def prevent_distractions(txt):
    lst = ("anime", "meme", "vines", "roasts", "Danny DeVito")
    for x in lst:
        if x in txt:
            return "NO!"

    return "Safe watching!"

print(prevent_distractions(txt))


#Task_6
lst = [3, 6, 12, 36]
def factor_chain(lst):
    lst1 = []
    for x in lst:
        if lst[-1] % x == 0:
            lst1.append(x)
    return len(lst) == len(lst1)

print(factor_chain(lst))


#Task_7
dates = ["Sept 22", "Sept 21", "Oct 15"]
month = input("Month: ")
def upload_count(dates,month):
    l = len(month)
    res = 0
    for i in dates:
        if i[:l] == month:
            res += 1
    return res

print(upload_count(dates,month))








