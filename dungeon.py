import random

hero = '@'
hero_x = 0
level = '..s.b..G.p...$..$..f..hm...r..N.W..$...r....$.D..W.'
level = list(level)
hunger = 0
money = 0
hp = 10
#                key  :        name          hunger        hp
food = {'s':('sweets',-7,0),
        'b':('beaf',-28,0),
        'p':('pork',-26,0),
        'f':('fish',-14,0),
        'r':('rotten beaf',-4,-2),
        'h':('small health potion',0,5),
        'm':('big health potion',0,10)}      


while hp > 0:
    for x, char in enumerate(level):
        if x == hero_x:
            print(hero, end='' )
        else:
            print(char, end='' )
    print()
    hunger +=1
    if hunger >100:
        break
    command = input('Hunger: {} Money:{} HP{},your command?'.format(hunger,money,hp))
    if command == 'quit' or command == 'exit' or command == 'stop':
        break
    elif command == 'a':
        hero_x-=1
    elif command == 'd':
        hero_x+=1 
        
    elif command == 'D':
        hero_x+=2
    elif command == 'A':
        hero_x-=2 
    elif command == 'superjump':
        hero_x-=10
    elif command == 'hyperjump':
        hero_x+=10    
    elif command == 'hyperhypersuperjump':      
        hero_x+=100
    elif command == 'supersuperhyperjump':    
        hero_x-=100
    elif command == 'randomjump':
        hero_x=random.randint(-10,10)
    # ------------------------auswertung------------------------------
    stuff = level[hero_x]
    if stuff in food:
        print('you eat: ', food[stuff][0])
        hunger+= food[stuff][1]
        hp+= food[stuff][2]
        level[hero_x]='.'
    elif stuff =='$':
        print('Money,money,money')
        money+=random.randint(1,30)
        level[hero_x]='.'
            
