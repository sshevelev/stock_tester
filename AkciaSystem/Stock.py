'''
Created on 09.01.2012

@author: ����
������ - �����
������ � ���� ��� ���������� �� �����:
������������, ����, ������ ��������, ������ ���������
'''
class Balance:
    def __init__(self,Date,I,II,III,Prib):
        self.Data=Date;
        self.I=I;
        self.II=II;
        self.III=III;
        self.Prib=Prib;
    

class Kotirovka:
    def __init__(self,Date,ClosePrice):
        self.Date=Date;
        self.ClosePrice=ClosePrice;
        
class Stock:
    '''
    classdocs
    '''
    

    def __init__(self,name,site,listKotirovok,listBalance):
        '''
        Constructor
        '''
        self.name=name;
        self.site=site;
        self.listKotirovok=listKotirovok;
        self.listBalance=listBalance;
        
        
