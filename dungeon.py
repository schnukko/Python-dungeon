import random


hero = '@'
hero_x = 0
level = '..s.b..G.p...$..$..f.....r..N.W..$...r....$.D..W.'
level = list(level)
hunger = 0
money = 0
hp = 10

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
    if level[hero_x]=='s':
        print('You eat a box of sweets.')
        hunger -= 7
        level[hero_x]='.'
    elif level[hero_x]=='b':
        print('Such a good beaf')
        hunger -= 28
        level[hero_x]='.'
    elif level[hero_x]=='p':
        print('A good pork')
        hunger -= 26
        level[hero_x]='.'
    elif level[hero_x]=='f':
        print('Tasty fish')
        hunger -= 14
        level[hero_x]='.'  
    elif level[hero_x]=='r':
        print('Ihh!Rotten beaf')
        hunger -= 4
        hp -=2
        level[hero_x]='.'
    elif level[hero_x]=='$':
        print('Money,money,money')
        money+=random.randint(1,30)
        level[hero_x]='.'
            
