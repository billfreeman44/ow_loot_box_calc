import json
import operator

def recurprint(data,poststr,f):
    if type(data) != dict and type(data) != list:
        if 'items' in poststr+data:
            f.write(poststr+data+'\n')          
            #print poststr+data
        return
    if type(data) == dict:
        for key in data:
            recurprint(data[key],poststr+key+'|',f)
    if type(data) == list:#WHO MAKES A LIST OF DICKS
        for item in data:
            f.write('\n')        
            #print 
            recurprint(item,poststr,f)
            
def heroToNum(herostr):
    heroes=['ana','bastion','dva','genji',\
            'hanzo','junkrat','lucio','mccree',\
            'mei','mercy','orisa','pharah','reaper',\
            'reinhardt','roadhog','soldier-76','sombra',\
            'symmetra','torbjorn','tracer','widowmaker',\
            'winston','zarya','zenyatta','all']
    for i in range(len(heroes)):
        if heroes[i] == herostr:
            return i+1
    return -1

def rarityToNum(rarestr):
    rarities=['common','rare','epic','legendary']
    for i in range(len(rarities)):
        if rarities[i] == rarestr:
            return i+1
    return -1

def typeToNum(typestr):
    types=['icons','sprays','skins','emotes','intros','voicelines','poses']
    for i in range(len(types)):
        if types[i] == typestr:
            return i+1
    return -1

def eventToNum(eventstr):
    events=['HALLOWEEN_2016','SUMMER_GAMES_2016','UPRISING_2017','WINTER_WONDERLAND_2016','YEAR_OF_THE_ROOSTER_2017']
    for i in range(len(events)):
        if events[i] == eventstr:
            return i+1
    return -1
def achievementToNum(achievementstr):
    achievements=['true','blizzard']
    for i in range(len(achievements)):
        if achievements[i] == achievementstr:
            return i+1
    return -1


            
def addinfo(itemdic,arr):
    itemdic['he']=heroToNum(arr[0])
    itemdic['ty']=typeToNum(arr[2])
    if arr[3] == 'name':
        itemdic['na']=arr[4]
    if arr[3] == 'quality':
        itemdic['ra']=rarityToNum(arr[4])
#    if arr[3] == 'id': ##fuck id. using a number instead...
#        itemdic['id']=arr[4]
    if arr[3] == 'event':
        itemdic['ev']=eventToNum(arr[4])
    if arr[3] == 'achievement':
        itemdic['ac']=achievementToNum(arr[4])
    if arr[3] == 'standardItem':
        itemdic['de']=1
    return itemdic


def apply_defaults(itemdic):    
    if itemdic['ra']==0:
        if itemdic['ty']==typeToNum('sprays'):
            itemdic['ra']=rarityToNum('common')
        if itemdic['ty']==typeToNum('icons'):
            itemdic['ra']=rarityToNum('rare')
    



    #calculate costs for normies
    if itemdic['ev']==0 and itemdic['ac']==0 and itemdic['de']==0 and itemdic['ty'] != typeToNum('icons'):
        if itemdic['ra']==1:
            itemdic['co']=25
        elif itemdic['ra']==2:
            itemdic['co']=75
        elif itemdic['ra']==3:
            itemdic['co']=250
        elif itemdic['ra']==4:
            itemdic['co']=1000

    #calculate costs for eventos        
    if itemdic['ev']!=0 and itemdic['ac']==0 and itemdic['ty'] != typeToNum('icons'):
        if itemdic['ra']==1:
            itemdic['co']=75
        elif itemdic['ra']==2:
            itemdic['co']=225
        elif itemdic['ra']==3:
            itemdic['co']=750
        elif itemdic['ra']==4:
            itemdic['co']=3000



        

       
##    
##    if itemdic['event']=='unknown':
##        itemdic['event']='none'
        
    return itemdic


def explodestr(strin):
    x=strin.find('|')
    if x== -1:
        return ['INVALID']
    x=strin.split('|')
    y=x[:-1]
    y.append(x[-1][0:-1])
    return y

level=0
linearr=[]


with open('items.json') as json_data:
    data = json.load(json_data)
    ##help(data)
f=open('jsonoutput.txt','w')
recurprint(data,'',f)
f.close()

f=open('jsonoutput.txt','r')
itemtemplate={'hero':'unknown','type':'unknown',\
              'rarity':'unknown','event':'none',\
              'achievement':'none','cost':'0',\
              'dupval':'0','id':'0','iname':'0','getinbox':'yes','default':'no'}
itemtemplate={'he':0,'ty':0,\
              'ra':0,'ev':0,\
              'ac':0,'co':0,\
              'id':0,\
              'na':'idk',\
                 'de':0,'ck':0}
itemdic=itemtemplate
itemlist=[]
counter=1
for line in f:
    arr=explodestr(line)
    if arr[0] != 'INVALID':
        #pass
        #print arr
        itemdic=addinfo(itemdic,arr)
    else:
        #print itemdic
        if (itemdic['ty']==typeToNum('icons') and itemdic['he']!=heroToNum('all')) or itemdic['he'] == 0:
            pass
        else:
            itemdic=apply_defaults(itemdic)
            itemdic['id']=counter
            print itemdic
            itemlist.append(itemdic)
            counter+=1
        itemdic={'he':0,'ty':0,\
              'ra':0,'ev':0,\
              'ac':0,'co':0,\
              'id':0,\
              'na':'idk',\
                 'de':0,'ck':0}
## 'he' - hero heroToNum('all')
## 'ty' - type typeToNum('icons')
## 'ra' - rarity rarityToNum('common'
## 'ev' - event
## 'ac' - achievement
## 'co' - cost
## 'id' - id
## 'na' - name
## 'de' - default
## 'w'  - want checkmark
## 'h'  - havecheckmark


##handle the last item
itemdic=apply_defaults(itemdic)
itemdic['id']=counter
itemlist.append(itemdic)    


#sort stuff
itemlist.sort(key=operator.itemgetter('ac'))
itemlist.sort(key=operator.itemgetter('ev'))
itemlist.sort(key=operator.itemgetter('ra'))
itemlist.reverse()
itemlist.sort(key=operator.itemgetter('ty'))
itemlist.sort(key=operator.itemgetter('he'))

objectstr=''
for idd in itemlist:
    objectstr+=''+str(idd)+','

f.close()

f=open('item_output.js','w')



f.write('''
/*
## 'he' - HERO NUMBER: order (ana is 1) =
['ana','bastion','dva','genji',\

'hanzo','junkrat','lucio','mccree',\
            
'mei','mercy','orisa','pharah','reaper',\
            
'reinhardt','roadhog','soldier-76','sombra',\
            
'symmetra','torbjorn','tracer','widowmaker',\

'winston','zarya','zenyatta','all']
            
## 'ty' - TYPE ['icons','sprays','skins','emotes','intros','voicelines','poses']
## 'ra' - RARITY ['common','rare','epic','legendary']
## 'ev' - EVENT (0 is no event, 1 is halloween)....['HALLOWEEN_2016','SUMMER_GAMES_2016',
               'UPRISING_2017','WINTER_WONDERLAND_2016',
               'YEAR_OF_THE_ROOSTER_2017']
## 'ac' - ACHIEVEMENT ['true','blizzard']
## 'co' - COST
## 'id' - ID NUMBER
## 'na' - NAME
## 'de' - DEFAULT ITEM
## 'wck'  - CHECKBOX (0: no checks, 1: has check, 2: want,
3: has check and has disable, 4: no check want disable)

*/

''')

f.write('var itemarr=['+objectstr[:-1]+'];') #remove trailing comma
f.close()

