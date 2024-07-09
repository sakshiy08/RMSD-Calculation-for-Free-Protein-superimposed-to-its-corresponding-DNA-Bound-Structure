import numpy as np
f=open("alignedfile6_dna_protein.pdb")
p1c1=[]
p1c2=[]
p2c1=[]
p2c2=[]
d1c1=[];d1c2=[];d2c1=[];d2c2=[];
for line in f:
 if(line.split()[0]=='ATOM'):
  if(line.split()[2]=='P' and line.split()[4]=='A'):
   p1c1.append([float(line.split()[6]),float(line.split()[7]),float(line.split()[8])])
  if(line.split()[2]=='P' and line.split()[4]=='B'):
   p1c2.append([float(line.split()[6]),float(line.split()[7]),float(line.split()[8])])
  if(line.split()[2]=='P' and line.split()[4]=='C' and line.split()[5]!='1'):
   p2c1.append([float(line.split()[6]),float(line.split()[7]),float(line.split()[8])])
  if(line.split()[2]=='P' and line.split()[4]=='D'):
   p2c2.append([float(line.split()[6]),float(line.split()[7]),float(line.split()[8])])
  if(line.split()[2]=='CA' and line.split()[4]=='A'):
      d1c1.append([float(line.split()[6]),float(line.split()[7]),float(line.split()[8])])
  if(line.split()[2]=='CA' and line.split()[4]=='B'):
      d1c2.append([float(line.split()[6]),float(line.split()[7]),float(line.split()[8])])
  if(line.split()[2]=='CA' and line.split()[4]=='C'):
      d2c1.append([float(line.split()[6]),float(line.split()[7]),float(line.split()[8])])
  if(line.split()[2]=='CA' and line.split()[4]=='D'):
      d2c2.append([float(line.split()[6]),float(line.split()[7]),float(line.split()[8])])

print(len(p1c1),len(p1c2),len(p2c1),len(p2c2))
print(len(d1c1),len(d1c2),len(d2c1),len(d2c2))
sq_sum=0;psq_sum=0
for i in range(len(p1c1)):
 sq_sum+=(p1c1[i][0]-p2c1[i][0])**2+(p1c1[i][1]-p2c1[i][1])**2+(p1c1[i][2]-p2c1[i][2])**2
for i in range(len(p1c2)):
 sq_sum+=(p1c2[i][0]-p2c2[i][0])**2+(p1c2[i][1]-p2c2[i][1])**2+(p1c2[i][2]-p2c2[i][2])**2
for i in range(len(d1c1)):
 psq_sum+=(d1c1[i][0]-d2c1[i][0])**2+(d1c1[i][1]-d2c1[i][1])**2+(d1c1[i][2]-d2c1[i][2])**2
for i in range(len(d1c2)):
 psq_sum+=(d1c2[i][0]-d2c2[i][0])**2+(d1c2[i][1]-d2c2[i][1])**2+(d1c2[i][2]-d2c2[i][2])**2

mean_sq_sum=sq_sum/(len(p1c1)+len(p1c2))
root_mean_sq_sum=np.sqrt(mean_sq_sum)
print(mean_sq_sum,root_mean_sq_sum)

mean_psq_sum=psq_sum/(len(d1c1)+len(d1c2))
root_mean_psq_sum=np.sqrt(mean_psq_sum)
print(mean_psq_sum,root_mean_psq_sum)
