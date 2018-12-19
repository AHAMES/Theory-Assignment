# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 19:27:01 2018

@author: Ahmed
"""

stack=['$']

PDA={0:{1:{'input':'a','nextState':0,'pop':'#','push':'a'},
        2:{'input':'c','nextState':1,'pop':'#','push':'#'},
        3:{'input':'d','nextState':3,'pop':'#','push':'#'},'accept':False},
     1:{1:{'input':'b','nextState':1,'pop':'a','push':'#'},
        2:{'input':'#','nextState':2,'pop':'$','push':'#'},'accept':False},
     3:{1:{'input':'b','nextState':4,'pop':'a','push':'#'},
        2:{'input':'#','nextState':2,'pop':'$','push':'#'},'accept':False},
     4:{1:{'input':'b','nextState':3,'pop':'#','push':'#'},'accept':False},
     2:{'accept':True}}
        
currentState=0

tape='aaaadbbbbbbbb'
#raw_input('Enter your string: ')
stop=False

for i in tape:
    
    if stop==True:
        break
    else:
        index=0
        for j in PDA[currentState]:
            currentPush=PDA[currentState][j]['push']
            currentPop=PDA[currentState][j]['pop']
            currentInput=PDA[currentState][j]['input']
            if(PDA[currentState].keys()[index]=='accept'):
                stop=True
                break
            index+=0
            if(PDA[currentState][j]['input']==i):
                if(PDA[currentState][j]['pop']!='#'):
                   if(stack[-1]==PDA[currentState][j]['pop']):
                       stack.pop();
                   else:
                       stop=True
                       break
                if(PDA[currentState][j]['push']!='#'):
                   stack.append(PDA[currentState][j]['push'])
                break
                   
            else:
                continue
            
        currentState=PDA[currentState][j]['nextState']
           
index=0
if stack[-1]=='$' and stop==False:
    for j in PDA[currentState]:
        if(PDA[currentState].keys()[index]=='accept'):
            stop=True
            break
        index+=1
        if PDA[currentState][j]['pop']=='$':
            if(PDA[currentState][j]['push']=='#'):
               stack.pop();
               currentState=PDA[currentState][j]['nextState']
        if(PDA[currentState]['accept']==True):
            print 'Accept'
            break     
if PDA[currentState]['accept']==False or stop==True:
    print 'reject'
               
                    
                    
                    
                    
                    
                    
                    