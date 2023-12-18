import random

#user_win = 0 

def compare1():
    compare=[]
    a=0
    for _ in range (2):
        a=random.randint(0,49)
        compare.append(a)
        while a == compare[0]:
            a=random.randint(0,49)
        compare.append(a)
        return compare
    
def compare2(list):
    a=0
    for _ in range (2):
        a=random.randint(0,49)
        while a == list[0]:
            a=random.randint(0,49)
        return a
    

def chk_flw ( a,b,answer):
    #global user_win
    if answer=='a':
        if a['follower_count']>b['follower_count']:
            result="win"
            #user_win+=1
            return result
        elif a['follower_count']<b['follower_count']:
            result="loss"
            return result
        elif a['follower_count']==b['follower_count']:
            result="draw"
            return result
    elif answer=='b':
        if a['follower_count']<b['follower_count']:
            result="win"
            #user_win+=1
            return result
        elif a['follower_count']>b['follower_count']:
            result="loss"
            return result
        elif a['follower_count']==b['follower_count']:
            result="draw"
            return result
