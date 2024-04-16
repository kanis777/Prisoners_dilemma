import numpy as np
actions=["Deflect","Cooperate"]

states=["Deflect","Cooperate"]
rewards=[[1,-5],[-5,5]]



def calculate(lst):
    count1=0
    count2=0
    for i in range(len(lst)):
        if lst[i]=="Deflect":
            count1+=1
        else:
            count2+=1
    return count1,count2

def prevaction_calculate(lst):
    count1=0
    count2=0
    for i in range(len(lst),len(lst)-2):
        if lst[i]=="Deflect":
            count1+=1
        else:
            count2+=1
    if count2>count1:
        return "Cooperate"
    else:
        return "Deflect"
    



def myalgorithm(lst):

    deflects,cooperation=calculate(lst)
    #print(deflects,cooperation)
    prevaction=prevaction_calculate(lst)
    #print(prevaction)
    if deflects>cooperation and prevaction=="Deflect":
        return "Deflect"
    elif cooperation>deflects and prevaction=="Cooperate":
        return "Cooperate"
    elif deflects>cooperation and prevaction=="Cooperate":
        return "Deflect"
    else:
        return "Cooperate"

def titfortwotats(previous_action,before_previous):
    if previous_action=="Deflect":
        if before_previous=="Deflect":
            return "Deflect"
    return "Cooperate"



def always_cooperate():
    return "Cooperate"

def always_deflect():
    return "Deflect"


def generate_random():
    x=np.random.randint(len(actions))
    return actions[x]

def titfortat(previous_action):
    if previous_action=="Deflect":
        return "Deflect"
    return "Cooperate"

def update_rewards(reward1,reward2,action1,action2):
    if action1=="Deflect" and action1==action2:
        reward1+=1
        reward2+=1
    elif action2=="Cooperate" and action2==action1:
        reward1+=3
        reward2+=3
    elif action1=="Cooperate" and action2=="Deflect":
        reward1+=0
        reward2+=5
    else:
        reward1+=5
        reward2+=0
    return reward1,reward2



def myalgo_training():
    agent1=[]
    agent2=[]

    reward1=0
    reward2=0
    agent1.append("Deflect")
    agent2.append("Cooperate")
    reward1+=5
    reward2+=0
    num_rounds=1000

    agent1.append("Deflect")
    agent2.append("Cooperate")
    reward1+=5
    reward2+=0
    for _ in range(2,num_rounds):
        
        action1=myalgorithm(agent2)
        agent1.append[action1]
        #print(action1)
        
        



   
def second_training():
    agent1=[]
    agent2=[]

    reward1=0
    reward2=0
    agent1.append("Deflect")
    agent2.append("Cooperate")
    reward1+=5
    reward2+=0
    num_rounds=1000

    agent1.append("Deflect")
    agent2.append("Cooperate")
    reward1+=5
    reward2+=0
    num_rounds=1000
    for _ in range(2,num_rounds):
        prev=agent2[_-1]
        bef_prev=agent2[_-2]
        action1=titfortwotats(prev,bef_prev)
        #print(action1)
        agent1.append(action1)
        prev1=agent1[_-1]
        action2=titfortat(prev1)
        agent2.append(action2)
        reward1,reward2=update_rewards(reward1,reward2,action1,action2)
    print("Tit for Two Tats :",reward1)
    print("Tit for Tat      :",reward2)




def training():
    agent1=[]
    agent2=[]

    reward1=0
    reward2=0
    agent1.append("Deflect")
    agent2.append("Cooperate")
    reward1+=5
    reward2+=0
    num_rounds=1000
    for _ in range(1,num_rounds):
        prev=agent2[_-1]
        action1=titfortat(prev)
        agent1.append(action1)
        action2=generate_random()
        agent2.append(action2)
        reward1,reward2=update_rewards(reward1,reward2,action1,action2)
    print("Tit For Tat :",reward1)
    print("Random      :",reward2)


        

def third_training():
    agent1=[]
    agent2=[]
    reward1=0
    reward2=0


    agent1.append("Deflect")
    agent2.append("Cooperate")
    reward1+=5
    reward2+=0
   

    agent1.append("Deflect")
    agent2.append("Cooperate")
    reward1+=5
    reward2+=0
    num_rounds=1000
    for _ in range(2,num_rounds):
        prev=agent2[_-1]
        bef_prev=agent2[_-2]
        action1=titfortwotats(prev,bef_prev)
        agent1.append(action1)
        action2=myalgorithm(agent1)
        #print("Action 1",action1)
        #print("Action 2",action2)
        agent2.append(action2)
        reward1,reward2=update_rewards(reward1,reward2,action1,action2)
    print("Tit for Two Tats :",reward1)
    print("My Algorithm     :",reward2)



def fourth_training():
    agent1=[]
    agent2=[]
    reward1=0
    reward2=0


    agent1.append("Deflect")
    agent2.append("Cooperate")
    reward1+=5
    reward2+=0
   

    agent1.append("Deflect")
    agent2.append("Deflect")
    reward1+=3
    reward2+=3
    num_rounds=1000
    for _ in range(2,num_rounds):
        
        action1=always_deflect()
        agent1.append(action1)
        action2=myalgorithm(agent1)
        
        agent2.append(action2)
        reward1,reward2=update_rewards(reward1,reward2,action1,action2)
    print("Always Deflect :",reward1)
    print("My Algorithm   :",reward2)
training()
second_training()
third_training()
fourth_training()




