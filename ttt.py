# -*- coding: utf-8 -*-
"""
@author: Tom Marvolo Riddle

name - TIC TAC TOE
"""

import numpy
import random
import inspect

    
class ttt :
    
    'All methods and properties'  
    
    iteration = 0
    methodName = ""
    check = 0
    move = 0
    
    

    def __init__(self) :
        self.rowX = numpy.array([ ["X" , "X" , "X"] ])
        self.rowY = numpy.array([ ["Y" , "Y" , "Y"] ])
        
        self.X = numpy.array([["X"]]) ;
        
        self.Y = numpy.array([["Y"]]) ;
        
        self.ui = numpy.array([ ["." , "." , "."] , ["." , "." , "."] , ["." , "." , "."] ])

        while(self.check == 0) :
            ttt.getUserIp(self)
            ttt.generateRandom(self)
            if(self.check > 0) :
                break

    def checkCondition(self) :
        'Checks all conditions'
        rowCount = 0
        for x in self.ui : 
            for i in range(0 , 3) :    
                if(rowCount == 2) :
                    if( numpy.array_equal(self.ui[0][i], self.X[0][0]) and 
                       numpy.array_equal(self.ui[1][i], self.X[0][0]) and
                       numpy.array_equal(self.ui[2][i], self.X[0][0])
                       ) :
                        'Checks if X wins(Vertically) '
                        print("X wins")  
                        self.check += 1
                        
                    if( numpy.array_equal(self.ui[0][i], self.Y[0][0]) and 
                       numpy.array_equal(self.ui[1][i], self.Y[0][0]) and
                       numpy.array_equal(self.ui[2][i], self.Y[0][0])
                       ) :
                        'Checks if Y wins(Vertically) '
                        print("Y wins")  
                        self.check += 1
                        
                    if( (numpy.array_equal(self.ui[0][0], self.X[0][0]) and 
                       numpy.array_equal(self.ui[1][1], self.X[0][0]) and
                       numpy.array_equal(self.ui[2][2], self.X[0][0]) ) 
                        or
                        (numpy.array_equal(self.ui[0][2], self.X[0][0]) and 
                       numpy.array_equal(self.ui[1][1], self.X[0][0]) and
                       numpy.array_equal(self.ui[2][0], self.X[0][0]) )
                       ) :
                        'Checks if X wins(Diagonal1 - \ and / ) '
                        print("X wins")  
                        self.check += 1
                        
                    if( (numpy.array_equal(self.ui[0][0], self.Y[0][0]) and 
                         numpy.array_equal(self.ui[1][1], self.Y[0][0]) and
                         numpy.array_equal(self.ui[2][2], self.Y[0][0]) ) 
                            or
                        (numpy.array_equal(self.ui[0][2], self.Y[0][0]) and 
                         numpy.array_equal(self.ui[1][1], self.Y[0][0]) and
                         numpy.array_equal(self.ui[2][0], self.Y[0][0]) )
                        ) :
                        'Checks if Y wins(Diagonal1 - \ and / ) '
                        print("Y wins")  
                        self.check += 1
                        
                rowCount += 1
            
            if(numpy.array_equal(self.rowX[0] , x)) :
                'Checks if X wins(Horizontally) '
                print("X wins")
                self.check += 1
                                
                
            if(numpy.array_equal(self.rowY[0] , x)) :
                'Checks if Y wins(Horizontally) '
                print("Y wins")
                self.check += 1
                
            
            
                
        


    def setUIX(self):    
        
        'Place X to GUI at given location'
        
        if(self.ui[self.i , self.j] == ".") :    
            self.ui[self.i , self.j] = "X"        
            self.move += 1
            ttt.prtUI(self)
            
            
        else :
            curframe = inspect.currentframe()
            calframe = inspect.getouterframes(curframe, 4)
            self.methodName = calframe[1][3]
            if(self.methodName == "getUserIp") :
                ttt.getUserIp(self)
                
            if(self.methodName == "generateRandom") :
                ttt.getUserIp(self)
        
    def setUIY(self):  
        
        'Place Y to GUI at generated location'
        
        if(self.ui[self.i , self.j] == ".") :    
            self.ui[self.i , self.j] = "Y"
            self.move += 1
            ttt.prtUI(self)
            
        else :
            curframe = inspect.currentframe()
            calframe = inspect.getouterframes(curframe, 4)
            self.methodName = calframe[1][3]
            if(self.methodName == "getUserIp") :
                ttt.generateRandom(self)
                
            if(self.methodName == "generateRandom") :
                ttt.generateRandom(self)
        
    def getUserIp(self) :
        
        self.i = int(input("Enter i : "))
        self.j = int(input("Enter j : "))
        
        print()
        print()
        
        if(self.i < 3 and self.j < 3) :    
            ttt.setUIX(self)
        else :
            print("Enter valid choice : ")
            ttt.getUserIp(self)
        
    def generateRandom(self) :
        
        
        self.i = random.randint(0 , 2)
        self.j = random.randint(0 , 2)
        
        ttt.setUIY(self)
        
        
    def prtUI(self) :
        if(self.move == 9) :
            self.check += 1
        ttt.checkCondition(self)
        self.iteration += 1
        print("Iteration : " , self.iteration)
        for x in self.ui :
            for y in x :
                print(y , end =" ")
            print() 
            
        print() 
        print() 
        
            
            
a = ttt() 


    
    
    
