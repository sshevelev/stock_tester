'''
Created on 09.01.2012

@author: УСЗН
Класс принятия решений.
На входе имеет список доступных для работы акций
На выходе отдает список годных для работы акций
'''
import Akcia;

class SPR:
    '''
    classdocs
    
    '''


    def __init__(self,listAkcia=None):
        '''
        Constructor
        '''
        self.listAkcia=listAkcia;
    
    def IsGoodAkcia(self,AkciaItem):
        if (AkciaItem.listBalance[0].I>AkciaItem.listBalance[0].II):
            return False;
        
        return True;
        
    def GetGoodAkcia(self):
        listGood = [];
        for x in self.listAkcia:
            if self.IsGoodAkcia(x):
                listGood.Append(x);
        return listGood;
    
            
            
         
        