#some code for the day

#VALORANT economy calculator

money=int(input("enter the amount of creds for the current round"))

if  money<4000:
    print("It is a pistol round. Opt for ghosts and some util")
elif 4000<money<10200:
    print("Economy is damagaed. Full save or opt for ghost/util")
    
elif 10200<money<20000:
    print("Economy is somewhat healthy, buy semi rifles and util")
    
elif 20000<money<30000:
    print("Economy is very healthy, buy rifles or operator and full util")
elif 30000<money<45000:
    print("Any util/weapon can be bought along with extra guns for gun change")
    
else:
    print("Please enter values of the correct type")
    
    
print()