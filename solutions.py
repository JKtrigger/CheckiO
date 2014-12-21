# -*- coding: cp1251 -*-
#Einstain problem
colors        = ['blue', 'green', 'red', 'white', 'yellow']
pets          = ['cat', 'bird', 'dog', 'fish', 'horse']
potables      = ['beer', 'coffee', 'milk', 'tea', 'water'] 
cigarettes    = ['Rothmans', 'Dunhill', 'Pall Mall', 'Winfield' , 'Marlboro']
person        = ['Brit', 'Dane', 'German', 'Norwegian', 'Swede'] 
num           = ['1','2','3','4','5']
# allinone
point         = [colors,pets,potables,cigarettes,person,num]  


def checkio(data,question):
    #generate all posible combinations
    Spisoc = []
    for c in colors:
        for p in pets:
            for pot in potables:
                for ci in cigarettes:
                    for per in person:
                        for n in num:
                            a = [c,p,pot,ci,per,n]
                            Spisoc.append(a)
    print '#generate all posible combinations'        
    #get IO data
    IO = []
    for d in data:
        x,y = d.split('-')
        IO.append([x,y])

    print'#get IO data' 
    #   define filters items
    filters = []
    for l in point:
        for c in IO:
            if c[0] in  l:
                #print set(l)-set([c[0]]),c[1]
                {filters.append([c[1],i]) for i in set(l)-set([c[0]])}
                    
            if c[1] in  l:
                #print set(l)-set([c[1]]),c[0]
                {filters.append([c[0],i]) for i in set(l)-set([c[1]])}

    badanswer = []
    
    print '#define filters items'
    #separete list by filters
    for z in Spisoc:
        for r in filters:
            if (r[0] in z and r[1] in z) and badanswer.count(z)==0:
                badanswer.append(z)
    print '#separete list by filters'        
    beforeanswer = [ix for ix in  Spisoc if ix not in badanswer]
   
    #print beforeanswer
    print '#get answer'
    sourse,answer  = question[0].split('-')
    ir = [iss for iss in beforeanswer if sourse in iss]
    tr = [ig for ig in eval(answer) if ig in ir[0]]
    
    
    return tr[0]
    
    #"Answer"
if __name__ == '__main__':
    assert checkio(['Norwegian-Dunhill','Marlboro-blue','Brit-3',
                    'German-coffee','beer-white','cat-water',
                    'horse-2','milk-3','4-Rothmans',
                    'dog-Swede','Norwegian-1','horse-Marlboro',
                    'bird-Brit','4-green','Winfield-beer',
                    'Dane-blue','5-dog','blue-horse',
                    'yellow-cat','Winfield-Swede','tea-Marlboro'],['fish-colors'])=='green' #1st test
    assert checkio(['Norwegian-Dunhill','Marlboro-blue','Brit-3',
                    'German-coffee','beer-white','cat-water',
                    'horse-2','milk-3','4-Rothmans',
                    'dog-Swede','Norwegian-1','horse-Marlboro',
                    'bird-Brit','4-green','Winfield-beer',
                    'Dane-blue','5-dog','blue-horse',
                    'yellow-cat','Winfield-Swede','tea-Marlboro'],['tea-num'])=='2' #2st test
    assert checkio(['Norwegian-Dunhill','Marlboro-blue','Brit-3',
                    'German-coffee','beer-white','cat-water',
                    'horse-2','milk-3','4-Rothmans',
                    'dog-Swede','Norwegian-1','horse-Marlboro',
                    'bird-Brit','4-green','Winfield-beer',
                    'Dane-blue','5-dog','blue-horse',
                    'yellow-cat','Winfield-Swede','tea-Marlboro'],['Norwegian-potables'])=='water' #3st test

    
    
                        
