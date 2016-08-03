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

import random
import numpy
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

#percent PER item, not per loot box. (x100)
p_common=5866
p_rare=3169
p_epic=722
p_leg=243

n_boxes_max=50000
n_trials_max=2000


# 6 leg skins, 6 epic skins
#highlight intros = epic (3)
#emotes = epic (3)
#victory poses = rare (9)
#profile pics = rare (39)
#voice lines = common (22) 
## updated values?
total_leg=6
total_epic=12
total_rare=48
total_common=22
##
##total_leg=6
##total_epic=1
##total_rare=1
##total_common=1

boxes_needed=[]

print "running"
for i in range(n_trials_max):
    leg_have=0.0
    epic_have=0.0
    rare_have=0.0
    common_have=0.0
    
    box_number=0
    got_all_items=0
    while got_all_items == 0 and box_number < n_boxes_max:
        box_number=box_number+1
        rarity_num=random.randint(0,9999)
        duplicate_chance=random.random()
        
        if rarity_num < p_leg:
            if leg_have/total_leg < duplicate_chance:
                leg_have=leg_have+1
            
        elif rarity_num < p_leg+p_epic:
            if epic_have/total_epic < duplicate_chance:
                epic_have=epic_have+1
                
        elif rarity_num < p_leg+p_epic+p_rare:
            if rare_have/total_rare < duplicate_chance:
                rare_have=rare_have+1
        else:
            if common_have/total_common < duplicate_chance:
                common_have=common_have+1

        if total_common == common_have and total_leg == leg_have \
           and total_rare == rare_have and total_epic == epic_have:
            got_all_items=1

    
    boxes_needed.append(box_number)
#=================== end of main loopskie
    
boxes_needed=sorted(boxes_needed)
xarr=range(len(boxes_needed))

plt.plot(xarr,boxes_needed)
plt.ylabel('# of summer items')
plt.xlabel('simulation number')
plt.show()
plt.ylabel('normalized # of people')
plt.xlabel('# of summer items')
n, bins, patches = plt.hist(boxes_needed, 50, normed=1, facecolor='green')
plt.show()


print "final statistics"
print
print "min: "+str(min(boxes_needed))
for i in [0.01,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,0.99]:
    print str(i*100)+"th percentile: "+ \
          str(boxes_needed[int(round(n_trials_max*i))])
print "average: "+str(numpy.mean(boxes_needed))
print "median: "+str(numpy.median(boxes_needed))
#print "std dev: "+str(numpy.stdev(boxes_needed))













