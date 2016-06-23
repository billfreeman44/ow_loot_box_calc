

print "test"


#PLAN!
# USE random numbers to
#simulate loot box openings

#use percentages from reddit for each rarity
#use random numbers to decide rarity of each
#item found.

#assume item distribution is even
#(each legendary has same chance of appearing
#if loot box gives a legendary item)

#account for duplicates

#once enough money to buy remaining items, simulation stops.

import random
import numpy
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

#percent PER item, not per loot box. (x100)
p_common=5866
p_rare=3169
p_epic=722
p_leg=243

n_boxes_max=20000
n_trials_max=1000

n_heroes=21

#number of skins per hero
n_leg=4
n_epic=2
n_rare=4
n_common=1
n_sprays=25 #common
n_emotes=3 #rare
n_voicelines=9
n_victoryposes=3 #rare
n_intros=3 #epic

total_leg=n_heroes*n_leg
total_epic=n_heroes*n_epic*n_intros
total_rare=n_heroes*n_rare*n_emotes*n_victoryposes
total_common=n_heroes*n_sprays*n_voicelines

print total_leg
print total_epic
print total_rare
print total_common


#player icons
n_p_icons=45 #rarity?



#duplicate gold
dup_common=5
dup_rare =15
dup_epic =50
dup_leg =200

#cost of buying items
common_cost=25
rare_cost=75
epic_cost=250
leg_cost=1000

boxes_needed=[]


for i in range(n_trials_max):
    if int(i/100) == 0:
        print i
        
    leg_have=0.0
    epic_have=0.0
    rare_have=0.0
    common_have=0.0
    gold_have=0.0
    
    box_number=0
    got_all_items=0
    while got_all_items == 0 and box_number < n_boxes_max:
        box_number=box_number+1
        rarity_num=random.randint(0,9999)
        duplicate_chance=random.random()
        if rarity_num < p_leg:
            #print 'LEGENDARY'
            #print leg_have/total_leg
            if leg_have/total_leg < duplicate_chance:
                leg_have=leg_have+1
            else:
                gold_have=gold_have+dup_leg
            
        elif rarity_num < p_leg+p_epic:
            #print 'EPIC'
            #print epic_have/total_epic , duplicate_chance
            if epic_have/total_epic < duplicate_chance:
                epic_have=epic_have+1
            else:
                gold_have=gold_have+dup_epic
                
        elif rarity_num < p_leg+p_epic+p_rare:
            #print 'rare'
            if rare_have/total_rare < duplicate_chance:
                rare_have=rare_have+1
            else:
                gold_have=gold_have+dup_rare
                
        #elif rarity_num < p_leg+p_epic+p_rare+p_common:
        else:
            #print 'common'
            if common_have/total_common < duplicate_chance:
                common_have=common_have+1
            else:
                gold_have=gold_have+dup_common
        #check if we can buy the rest of the items.
        gold_needed=(total_leg - leg_have) * leg_cost
        gold_needed=gold_needed + (total_epic - epic_have) * epic_cost
        gold_needed=gold_needed + (total_rare - rare_have) * rare_cost
        gold_needed=gold_needed + (total_common - common_have) * common_cost
        if gold_have >= gold_needed:
            #print "WE HAVE ALL THE ITEMS"
            #print 'in the '+str(box_number/4)+'rd box'
            got_all_items=1
    #print "final stats:"
    #print "total gold: "+str(int(gold_have))
    #print "total legendary: "+str(int(leg_have))
    #print "total epic: "+str(int(epic_have))
    #print "total rare: "+str(int(rare_have))
    #print "total common: "+str(int(common_have))
    
    boxes_needed.append(box_number/4.0) 

n, bins, patches = plt.hist(boxes_needed, 50, normed=1, facecolor='green')



print "final statistics"
print
print "average: "+str(numpy.mean(boxes_needed))
print "median: "+str(numpy.median(boxes_needed))
#print "std dev: "+str(numpy.stdev(boxes_needed))



plt.show()









