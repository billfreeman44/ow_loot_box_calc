

def gaus(x,a,x0,sigma):
    return a*exp(-(x-x0)**2/(2*sigma**2))

#true if loop should end
def endloop(item_have,item_count,need_icons,event,n_boxes_max,box_number):
    #check box maximum
    if box_number > n_boxes_max:
        return True
    #Check if have all icons
    if need_icons:
        if item_have['icon'] == item_count['icon']:
            if event:
                if item_have['icon-event'] == item_count['icon-event']:
                    return True
            else:
                return True
    #check if you have enough money to buy everything left.
    else:
        gold_needed = \
                    ( item_count['common'] - item_have['common'] ) * cost['common'] \
                  + ( item_count['rare'] - item_have['rare'] ) * cost['rare'] \
                  + ( item_count['epic'] - item_have['epic'] ) * cost['epic'] \
                  + ( item_count['leg'] - item_have['leg'] ) * cost['leg']
        if event:
            gold_needed = gold_needed \
                  + ( item_count['common-event'] - item_have['common-event'] ) * cost['common-event'] \
                  + ( item_count['rare-event'] - item_have['rare-event'] ) * cost['rare-event'] \
                  + ( item_count['epic-event'] - item_have['epic-event'] ) * cost['epic-event'] \
                  + ( item_count['leg-event'] - item_have['leg-event'] ) * cost['leg-event']
        if item_have['gold'] >= gold_needed:
            return True
        
    return False
        

def add_item(rarity_chance,duplicate_chance,probabilities,item_have,item_count,event,dup_gold,gold_drop):
    poststr=''
    if event:
        if random.random() < probabilities['p-event']:
            poststr='-event'
        
    if rarity_chance < probabilities['leg']:
        if float(item_have['leg'+poststr])/item_count['leg'+poststr] < duplicate_chance:
            item_have['leg'+poststr]=item_have['leg'+poststr]+1
        else:
            item_have['gold']=item_have['gold']+dup_gold['leg']
        
    elif rarity_chance < probabilities['leg']+probabilities['epic']:
        if float(item_have['epic'+poststr])/item_count['epic'+poststr] < duplicate_chance:
            item_have['epic'+poststr]=item_have['epic'+poststr]+1
        else:
            item_have['gold']=item_have['gold']+dup_gold['epic']
            
    elif rarity_chance < probabilities['leg']+probabilities['epic']\
         +probabilities['rare']:
        if float(item_have['rare'+poststr])/item_count['rare'+poststr] < duplicate_chance:
            item_have['rare'+poststr]=item_have['rare'+poststr]+1
        else:
            item_have['gold']=item_have['gold']+dup_gold['rare']
            
    elif rarity_chance < probabilities['leg']+probabilities['epic']\
         +probabilities['rare']+probabilities['common']:
        #check if icon
        if random.random() < float(item_count['icon'+poststr])/(item_count['icon'+poststr]+item_count['common'+poststr]):
            #check if duplicate icon
            if float(item_have['icon'+poststr])/item_count['icon'+poststr] < duplicate_chance:
                item_have['icon'+poststr]=item_have['icon'+poststr]+1
            else:
                item_have['gold']=item_have['gold']+dup_gold['common']
        
        if float(item_have['common'+poststr])/item_count['common'+poststr] < duplicate_chance:
            item_have['common'+poststr]=item_have['common'+poststr]+1
        else:
            item_have['gold']=item_have['gold']+dup_gold['common']
        
    elif rarity_chance < probabilities['leg']+probabilities['epic']\
         +probabilities['rare']+probabilities['common']\
         +probabilities['rare-currency']:
        item_have['gold']=item_have['gold']+gold_drop['rare']

    elif rarity_chance < probabilities['leg']+probabilities['epic']\
         +probabilities['rare']+probabilities['common']\
         +probabilities['rare-currency']+probabilities['epic-currency']:
        item_have['gold']=item_have['gold']+gold_drop['epic']

    elif rarity_chance < probabilities['leg']+probabilities['epic']\
         +probabilities['rare']+probabilities['common']\
         +probabilities['rare-currency']+probabilities['epic-currency']+probabilities['leg-currency']:
        item_have['gold']=item_have['gold']+gold_drop['leg']
        
    return item_have


def get_str(instr):
    ind1=instr.find("\"")
    ind2=instr.find("\"", ind1+1)
    return instr[ind1+1:ind2]


def get_str2(instr):
    ind1=instr.find("\"")
    ind2=instr.find("\"", ind1+1)
    ind3=instr.find("\"", ind2+1)
    ind4=instr.find("\"", ind3+1)
    return instr[ind3+1:ind4]

def printinfo(levelstr,infoarr,item_count):
    hero=levelstr[2]
    kind=levelstr[4]
    
    event='none'
    for info in infoarr:
        if 'event' in info:
            event=info[6:]
            
    achievement='no'
    for info in infoarr:
        if 'achievement' in info:
            achievement='yes'
            
    idd='unknown'
    for info in infoarr:
        if 'id' in info:
            idd=info[3:]
            
    name='unknown'
    for info in infoarr:
        if 'name' in info:
            name=info[5:]
            
    quality='common'
    for info in infoarr:
        if 'quality' in info:
            quality=info[8:]
            
    standardItem='no'
    for info in infoarr:
        if 'standardItem' in info:
            standardItem='yes'
    
##    if kind != 'icons':
##        print hero+'|'+kind+'|'+name+'|'+idd+'|'+quality+'|'+event+'|'+achievement
##    elif hero == 'all':
##        print hero+'|'+kind+'|'+name+'|'+idd+'|'+quality+'|'+event+'|'+achievement
        
    if achievement == 'no':
        if event == 'none' and standardItem == 'no':
            if quality == 'epic':
                item_count['epic']+=1
            if quality == 'legendary':
                item_count['leg']+=1
            if quality == 'rare':
                item_count['rare']+=1
            if quality == 'common':
                if kind == 'icons' and hero == 'all':
                    item_count['icon']+=1
                if kind != 'icons':
                    item_count['common']+=1

        if event != 'none' and standardItem == 'no': ##uncomment for all items.
        #if event == 'UPRISING_2017' and standardItem == 'no':
            if quality == 'epic':
                item_count['epic-event']+=1
            if quality == 'legendary':
                item_count['leg-event']+=1
            if quality == 'rare':
                item_count['rare-event']+=1
            if quality == 'common':
                if kind == 'icons' and hero == 'all':
                    item_count['icon-event']+=1
                if kind != 'icons':
                    item_count['common-event']+=1
                
    return item_count



#read in a json file to count number of items
#https://github.com/Js41637/Overwatch-Item-Tracker/blob/master/data/items.json
#I changed quotes in items to single quotes. and changed true to "true"
#
item_count={'common':0, 'rare':0, 'leg':0, 'epic':0, \
    'common-event':0, 'rare-event':0, 'leg-event':0, 'epic-event':0, \
    'icon':0, 'icon-event':0}

   
level=0
linearr=[]
#the json library refused to read this in.
#I couldn't figure out the bug so I just did it "by hand"
with open('items.json') as json_data:
    for line in json_data:
        linearr.append(line)
    

levelstr=['','','','','','','','','','','']
infoarr=[]
for line in linearr:
    if "{" in line or "[" in line:
        level=level+1
    if "}" in line or "]" in line:
        if len(infoarr) >=2:
            item_count=printinfo(levelstr,infoarr,item_count)
        level=level-1
        infoarr=[]
    
    if "\"" in line:
        if line.count("\"") == 4:
            #outstr=''
            #for boop in levelstr[0:level+1]:
            #    if boop != '':
            #        outstr=outstr+boop+' '
            #outstr=outstr+get_str(line)+' '+get_str2(line)
            #print outstr + str(level)
            infoarr.append(get_str(line)+' '+get_str2(line))
        if line.count("\"") == 2:
            levelstr[level]=get_str(line)
                
        

#print item_count


#============================================================
#============================================================
#============================================================
#output some statistics and define costs etc...



#percent PER item, not per loot box. (x100)
probabilities={'common':5839,'rare':2710,'epic':537,'leg':218, \
            'rare-currency':411,'epic-currency':243,'leg-currency':42, \
            'p-event':0.3} #30 percent

print probabilities['common'] \
      + probabilities['rare'] \
      + probabilities['epic'] \
      + probabilities['leg'] \
      + probabilities['rare-currency'] \
      + probabilities['epic-currency'] \
      + probabilities['leg-currency'] #should add up to 10000


#duplicate gold
dup_gold={'common':5,'rare':15,'epic':50,'leg':200}

#cost of buying items
cost={'common':25,'rare':75,'leg':250,'epic':1000, \
      'common-event':75,'rare-event':225,'leg-event':750,'epic-event':3000}


#gold drops
gold_drop={'rare':50,'epic':150,'leg':500}


## Show number of items and total cost
print
print 'Number of commons: '+str(item_count['common'])
print 'Number of icons: '+str(item_count['icon'])
print 'Number of rares: '+str(item_count['rare'])
print 'Number of epics: '+str(item_count['epic'])
print 'Number of legendaries: '+str(item_count['leg'])
print
print 'Number of event commons: '+str(item_count['common-event'])
print 'Number of event icons: '+str(item_count['icon-event'])
print 'Number of event rared: '+str(item_count['rare-event'])
print 'Number of event epic: '+str(item_count['epic-event'])
print 'Number of event legendaries: '+str(item_count['leg-event'])
print

total_cost = item_count['common']*cost['common']
total_cost = total_cost + item_count['rare']*cost['rare']
total_cost = total_cost + item_count['epic']*cost['epic']
total_cost = total_cost + item_count['leg']*cost['leg']
print 'total cost for normal items: '+str(total_cost)


event_cost = item_count['common-event']*cost['common-event']
event_cost = event_cost + item_count['rare-event']*cost['rare-event']
event_cost = event_cost + item_count['epic-event']*cost['epic-event']
event_cost = event_cost + item_count['leg-event']*cost['leg-event']

print 'total cost for event items: '+str(event_cost)
print 'total cost for normal + event items: '+str(event_cost+total_cost)









#============================================================
#============================================================
#============================================================ 
#begin calculating number of loot boxos needed.
import random
import numpy
#import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

#need all icons
need_icons=True


#event is live
event=True


n_boxes_max=500000 #prevent bad luck.
n_trials=5000



boxes_needed=[]
print "running"
for i in range(n_trials):
    #print i
    #reset vars.
    item_have={'common':0, 'rare':0, 'leg':0, 'epic':0, \
        'common-event':0, 'rare-event':0, 'leg-event':0, 'epic-event':0, \
        'icon':0, 'icon-event':0,'gold':0}
    box_number=0
    while endloop(item_have,item_count,need_icons,event,n_boxes_max,box_number) == False:
        #print box_number
        box_number=box_number+1
        rarity_chance=random.randint(0,9999) #includes endpoints
        duplicate_chance=random.random()
        
        item_have=add_item(rarity_chance,duplicate_chance,\
                           probabilities,item_have,item_count,event,dup_gold,gold_drop)
        #print item_have

##    print
##    print 'Number of common items: '+str(item_have['common'])+'/'+str(item_count['common'])
##    print 'Number of icons: '+str(item_have['icon'])+'/'+str(item_count['icon'])
##    print 'Number of rare items: '+str(item_have['rare'])+'/'+str(item_count['rare'])
##    print 'Number of legendary items: '+str(item_have['leg'])+'/'+str(item_count['leg'])
##    print 'Number of epic items: '+str(item_have['epic'])+'/'+str(item_count['epic'])
##    print
##    print 'Number of event common items: '+str(item_have['common-event'])+'/'+str(item_count['common-event'])
##    print 'Number of event icons: '+str(item_have['icon-event'])+'/'+str(item_count['icon-event'])
##    print 'Number of event rare items: '+str(item_have['rare-event'])+'/'+str(item_count['rare-event'])
##    print 'Number of event legendary items: '+str(item_have['leg-event'])+'/'+str(item_count['leg-event'])
##    print 'Number of event epic items: '+str(item_have['epic-event'])+'/'+str(item_count['epic-event'])
##    print

        
    boxes_needed.append(box_number/4.0) 

n, bins, patches = plt.hist(boxes_needed, 50, normed=1, facecolor='green')



print "final statistics"
print
print "average: "+str(numpy.mean(boxes_needed))
print "median: "+str(numpy.median(boxes_needed))




plt.show()









