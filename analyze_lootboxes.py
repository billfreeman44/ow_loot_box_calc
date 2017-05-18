


f=open('box_statistics.txt','r')

itemarr=[]

nocommon_count=0
boxes_noleg=0
boxes_noleg_max=0
boxes_noleg_arr=[]

for line in f:
    #print line
    if line[0] in ['1','2','3','4','5','6','7']:
        #print line[0]
        itemarr.append(line[0])
        itemarr.append(line[1])
        itemarr.append(line[2])
        itemarr.append(line[3])
        if '1' not in line:
            nocommon_count+=1
        #if '4' in line or '7' in line:
        if '4' in line:
            boxes_noleg_arr.append(boxes_noleg)
            if boxes_noleg > boxes_noleg_max:
                boxes_noleg_max=boxes_noleg
            boxes_noleg=-1
        boxes_noleg+=1

print len(itemarr)
print len(itemarr)/4


print '1 = '+str(itemarr.count('1'))
print '2 = '+str(itemarr.count('2'))
print '3 = '+str(itemarr.count('3'))
print '4 = '+str(itemarr.count('4'))
print '5 = '+str(itemarr.count('5'))
print '6 = '+str(itemarr.count('6'))
print '7 = '+str(itemarr.count('7'))
print 'all = '+str(len(itemarr))
print


print 'common item = '+str(round(float(itemarr.count('1'))*100/len(itemarr),2))
print 'rare item = '+str(round(float(itemarr.count('2'))*100/len(itemarr),2))
print 'epic item = '+str(round(float(itemarr.count('3'))*100/len(itemarr),2))
print 'leg item = '+str(round(float(itemarr.count('4'))*100/len(itemarr),2))
print 'rare currency = '+str(round(float(itemarr.count('5'))*100/len(itemarr),2))
print 'epic currency = '+str(round(float(itemarr.count('6'))*100/len(itemarr),2))
print 'Leg currency = '+str(round(float(itemarr.count('7'))*100/len(itemarr),2))
print 'all = '+str(len(itemarr)/len(itemarr))
print

print 'there were '+str(nocommon_count)+' boxes with no commons'
print



print 'commons = '+str(round(float(itemarr.count('1'))*100/len(itemarr),2))
print 'rare = '+str(round(float(itemarr.count('2')+itemarr.count('5'))*100/len(itemarr),2))
print 'epic = '+str(round(float(itemarr.count('3')+itemarr.count('6'))*100/len(itemarr),2))
print 'leg = '+str(round(float(itemarr.count('4')+itemarr.count('7'))*100/len(itemarr),2))
print 'all = '+str(len(itemarr)/len(itemarr))


print
print 100./99.0 #leg
print 100./234.0 #epic
print 100./422.0 #rar
print 100./823.0 #commn

print
print 'there was a '+str(boxes_noleg_max)+' box streak with no legendaries'
print boxes_noleg_arr



















