#This code takes values for map aspects and predicts the site you might have the best chance of taking with the
#least number of players lost
#the fundamental functions are made such that they can account for most competitive games
#with minimal change to code
#To run this program, use it in a python compiler(python 2.7+ recommended)

#function to calculate probability of success and generate stats.
def decide(maps,lastmap,rnd,players,mapno,fake):
    #searches through the given list of maps.
    def msearch(l,target,low,high):                    
        if low>high:
            return False
        else:
            mid=(low+high)//2
            if l[mid]==target:
                return mid
            else:
                if l[mid]>target:
                    return msearch(l,target,low,mid-1)
                else:
                    return msearch(l,target,mid+1,high)
    fconstant=(2/len(maps))*fake
    index=msearch(maps,lastmap,0,len(maps)-1)   
    #assigned a variable index to the index of the provided last map
    def ovsc(rnd):
        #calculates strategy failure/success given the round number it is used in
        if rnd%fake:
            return rnd
        else:
            return 0
        
    #the following component calculates failure percentage by calculating a failure constant inversely proportional to the
    #number of sites and proportional to the number of different strategies applied.
    #with every repetition of strategy
    #this is very generic but is still applicable where the map pool is large
    #
    if index<(len(maps)-1)/2:
        print("You can enter site",maps[len(maps)-1],"with a loss of atmost",players//mapno,"players")
        print("The overall chances of failure are",ovsc(rnd)*fconstant,"%")
    else:
        print("You can enter site",maps[0],"with a loss of atmost",players//mapno,"players")
        print("The overall chances of failure are",ovsc(rnd)*fconstant,"%")
fake=int(input("How many different strats do you intend to apply?: "))
mapname=str(input("Enter the map name: "))
roundno=int(input("Enter the roundno: "))
lastmap=str(input("Enter the last site you entered: "))
print("\n\n")
maplist=["icebox","bind","split","fracture","ascent","breeze"]

if mapname.lower()=="haven":
    decide(['a','b','c'],lastmap.lower(),roundno,5,3,fake)
elif mapname.lower() in maplist:
    decide(['a','b'],lastmap.lower(),roundno,5,3,fake)
else:
    print("enter correct details")
