import random
f = open("log.txt", "w")

fl = 150
fr = 150
rl = 180
rr = 180
steering = 0
kw = 0
bat_temp = 30
mot_temp = 30
inv_temp = 30
bias = 45
apps = 0
brake = 0
rpm = 0

#accel
for i in range(500):
    f.write(f'0 0 {fl} {fr} {rl} {rr} {steering} {kw} 0 0 {bat_temp} {mot_temp} {inv_temp} {bias} {apps} {brake} {rpm}\n')
    if apps<100:
        apps += 5
    if rpm<6000:
        rpm += 10
    if fl<200:
        fl += 5
        fr += 5
        rl -= 5
        rr -= 5
    if kw<=80:
        kw += 10
    bat_temp += random.randint(-1,1)
    mot_temp += random.randint(-1, 1)
    inv_temp += random.randint(-1, 1)
    
