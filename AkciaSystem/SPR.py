'''
Created on 09.01.2012

@author: ����
����� �������� �������.
�� ����� ����� ������ ��������� ��� ������ �����
�� ������ ������ ������ ������ ��� ������ �����
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
    
            
            
         
        