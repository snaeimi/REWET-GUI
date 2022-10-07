# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 21:20:14 2022

@author: snaeimi
"""

import pandas as pd

class Single_Crew():
    def __init__(self, crew_name, crew_type, base_x, base_y, cur_x, cur_y, crew_shift):
        definitions = {}
        definitions['crew_name']  = crew_name
        definitions['crew_type']  = crew_type
        definitions['cur_x']      = base_x
        definitions['cur_y']      = base_y
        definitions['base_x']     = cur_x
        definitions['base_y']     = cur_y
        definitions['shift_name'] = crew_shift
        self.definitions = definitions

class Policy(dict):
    def __init__(self):
        self.crew_data   = []
        self.crew_types  = set() #for GUI Only
        self.shift       = pd.DataFrame(columns=['begining', 'end'])
        self.entity      = {}
        self.entity_rule = {}
        self.sequence    = {'DISTNODE':[], 'GNODE':[], 'PIPE':[], 'PUMP':[], 'RESERVOIR':[], 'TANK':[]}
        self.priority    = {}
        #print(self.sequence)
        
    def add_shift(self, crew_name, crew_type, base_x, base_y, cur_x, cur_y, crew_shift):
        new_crew = Single_Crew(crew_name, crew_type, base_x, base_y, cur_x, cur_y, crew_shift)
        self.crew_data.append(new_crew)
    
    def fakeUp(self):
        self.shift.loc["N",'begining'] = 16
        self.shift.loc["N",'end'     ] = 8
        self.shift.loc["D",'begining'] = 8
        self.shift.loc["D",'end'     ] = 16
        
        self.crew_types.add('ct')
        
        self.entity_rule = {}
        self.entity_rule['major_break']=[('FILE', None, ['FH90', 'FH114']), ('damage_type', 'EQ', 'break')]
        self.entity['major_break'] = 'PIPE'
        
        p1 = [('inspect', 'trunk'), ('inspect', 'distr'), ('prereroute', 'major_break'), ('reroute', 'major_break'), ('prereroute', 'minor_break'), ('reroute', 'minor_break'), ('prereroute', 'major_leak'), ('reroute', 'major_leak'), ('prereroute', 'minor_leak'), ('reroute', 'minor_leak'), ('isolate', 'distr')]
        p2 = ['EPICENTERDIST', 'EPICENTERDIST', 'EPICENTERDIST', 'EPICENTERDIST', 'EPICENTERDIST', 'EPICENTERDIST', 'EPICENTERDIST', 'EPICENTERDIST', 'EPICENTERDIST', 'EPICENTERDIST', 'EPICENTERDIST']
        self.priority['WDInspector'] = pd.Series()
        self.priority['WDInspector'].loc[1] = p1
        self.priority['WDInspector'].loc[2] = p2
        
        p1 = [('repair', 'distr')]
        p2 = ['WaterSource']
        self.priority['WDRepair2'] = pd.Series()
        self.priority['WDRepair2'].loc[1] = p1
        self.priority['WDRepair2'].loc[2] = p2