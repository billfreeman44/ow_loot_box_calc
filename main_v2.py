

import random
import numpy
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


#toggle on (1) or off (0) the rule that
#each box must have at least one item better
#than a common
four_common_rule=0

#toggle if a box of 4 commons gives you a
#rare (1) or if it re-chooses until you
#get a non-common thing
rejected_common_gives_rare=0



#percent PER item, not per loot box. (x100)
p_common=5839
p_rare=2710
p_epic=537
p_leg=218
p_rare_currency=411
p_epic_currency=243
p_leg_currency=42

print p_common+p_rare+p_epic+p_leg+p_rare_currency+p_epic_currency+p_leg_currency


n_boxes_max=50000
n_trials_max=1000

n_heroes=21



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

#gold drops
rare_gold_drop=50
epic_gold_drop=150
leg_gold_drop=500

## updated values?
total_leg=n_heroes*4
total_epic=n_heroes*8
total_rare=n_heroes*7
total_common=n_heroes*35

total_common=total_common + 27 #add in all hero spray
total_rare = total_rare + 118 #add hero icons


print total_leg
print total_epic
print total_rare
print total_common

total_cost = total_common*common_cost
total_cost = total_cost + total_rare*rare_cost
total_cost = total_cost + total_epic*epic_cost
total_cost = total_cost + total_leg*leg_cost
print 'total cost'
print total_cost


boxes_needed=[]

print "running"
for i in range(n_trials_max):
    #print i    
    leg_have=0.0
    epic_have=0.0
    rare_have=0.0
    common_have=0.0
    gold_have=0.0

    box_contents=[]
    box_number=0
    got_all_items=0
    while got_all_items == 0 and box_number < n_boxes_max:
        #print box_number
        box_number=box_number+1
        rarity_num=random.randint(0,9999) #includes endpoints
        duplicate_chance=random.random()
        if len(box_contents) >= 4:
            box_contents=[]
        
        if rarity_num < p_leg:
            box_contents.append('leg')
            if leg_have/total_leg < duplicate_chance:
                leg_have=leg_have+1
            else:
                gold_have=gold_have+dup_leg
            
        elif rarity_num < p_leg+p_epic:
            box_contents.append('epic')
            if epic_have/total_epic < duplicate_chance:
                epic_have=epic_have+1
            else:
                gold_have=gold_have+dup_epic
                
        elif rarity_num < p_leg+p_epic+p_rare:
            box_contents.append('rare')
            if rare_have/total_rare < duplicate_chance:
                rare_have=rare_have+1
            else:
                gold_have=gold_have+dup_rare
                
        elif rarity_num < p_leg+p_epic+p_rare+p_common:
            if four_common_rule == 0:
                box_contents.append('common')
                #print 'common'
                if common_have/total_common < duplicate_chance:
                    common_have=common_have+1
                else:
                    gold_have=gold_have+dup_common
            else:#use the 4 common are not allowed rule.
                #if the box has three commons in it, reject this common item
                if len(box_contents) == 3:
                    if box_contents[0] == 'common' and box_contents[1] == 'common' and box_contents[2] == 'common':
                        #pass
                        if rejected_common_gives_rare == 1:
                            box_contents.append('rare')
                            if rare_have/total_rare < duplicate_chance:
                                rare_have=rare_have+1
                            else:
                                gold_have=gold_have+dup_rare
                            
                        #print 'COMMON ITEM SKIPPED'
                        else: # not rejected comon
                            box_number=box_number-1

                    #if all 3 items weren't commons
                    else:
                        box_contents.append('common')
                        if common_have/total_common < duplicate_chance:
                            common_have=common_have+1
                        else:
                            gold_have=gold_have+dup_common
                # there weren't 3 items in the box yet
                else: 
                    box_contents.append('common')
                    #print 'common'
                    if common_have/total_common < duplicate_chance:
                        common_have=common_have+1
                    else:
                        gold_have=gold_have+dup_common
            

        elif rarity_num < p_leg+p_epic+p_rare+p_common+p_rare_currency:
            box_contents.append('rare')
            gold_have=gold_have+rare_gold_drop

        elif rarity_num < p_leg+p_epic+p_rare+p_common+p_rare_currency+p_epic_currency:
            box_contents.append('epic')
            gold_have=gold_have+epic_gold_drop

        elif rarity_num < p_leg+p_epic+p_rare+p_common+p_rare_currency+p_epic_currency+p_leg_currency:
            box_contents.append('leg')
            gold_have=gold_have+leg_gold_drop

            
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









