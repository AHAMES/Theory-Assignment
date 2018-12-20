# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 17:40:58 2018

@author: Ahmed
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 01:32:57 2018

@author: Ahmed
"""

#solves x^2
x= raw_input('Enter your string in this format #x#: ')

turingMachine={0:{1:{'direction':1,'nextState':1,'read':'1','write':'x'},
                  2:{'direction':-1,'nextState':4,'read':'#','write':'#'},'accept':False},
               1:{1:{'direction':1,'nextState':1,'read':'1','write':'1'},
                  2:{'direction':1,'nextState':2,'read':'#','write':'#'},'accept':False},
               2:{1:{'direction':-1,'nextState':3,'read':'b','write':'0'},
                  2:{'direction':1,'nextState':2,'read':'0','write':'0'},'accept':False},
               3:{1:{'direction':-1,'nextState':3,'read':'0','write':'0'},
                  2:{'direction':-1,'nextState':3,'read':'#','write':'#'},
                  3:{'direction':-1,'nextState':3,'read':'1','write':'1'},
                  4:{'direction':1,'nextState':0,'read':'x','write':'x'},'accept':False},
               4:{1:{'direction':-1,'nextState':4,'read':'0','write':'0'},
                  2:{'direction':1,'nextState':5,'read':'x','write':'0'},
                  3:{'direction':1,'nextState':11,'read':'#','write':'0'},'accept':False},
               5:{1:{'direction':1,'nextState':5,'read':'0','write':'0'},
                  2:{'direction':1,'nextState':6,'read':'#','write':'#'},'accept':False},
               6:{1:{'direction':1,'nextState':7,'read':'0','write':'y'},
                  2:{'direction':-1,'nextState':10,'read':'1','write':'1'},'accept':False},
               7:{1:{'direction':1,'nextState':7,'read':'0','write':'0'},
                  2:{'direction':1,'nextState':8,'read':'1','write':'1'},
                  3:{'direction':-1,'nextState':9,'read':'b','write':'1'},'accept':False},
               8:{1:{'direction':1,'nextState':8,'read':'1','write':'1'},
                  2:{'direction':-1,'nextState':9,'read':'b','write':'1'},'accept':False},
               9:{1:{'direction':-1,'nextState':9,'read':'1','write':'1'},
                  2:{'direction':-1,'nextState':9,'read':'0','write':'0'},
                  3:{'direction':1,'nextState':6,'read':'y','write':'y'},'accept':False}, 
               10:{1:{'direction':-1,'nextState':10,'read':'y','write':'0'},
                   2:{'direction':-1,'nextState':10,'read':'#','write':'#'},
                   3:{'direction':-1,'nextState':4,'read':'0','write':'0'},'accept':False},    
               11:{'accept':True}}             

tape=list(x)
index=1
currentState=0
f=0
while True:
    if turingMachine[currentState]['accept']==True:
        count=0;
        for i in tape:
            if i=='1':
                count+=1
        print count
        print "".join(tape)
        break
    for i in turingMachine[currentState]:
       
        if turingMachine[currentState][i]['read']==tape[index]:
            direction=turingMachine[currentState][i]['direction']
            if (index+direction)==len(tape)-1:
                tape.append('b')
            tape[index]=turingMachine[currentState][i]['write']
            currentState=turingMachine[currentState][i]['nextState']
            index+=direction
            break