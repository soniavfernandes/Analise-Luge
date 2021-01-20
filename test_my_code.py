# -*- coding: utf-8 -*-

import unittest
from analise_estatistica_luge import column_velocity
import os
import pandas as pd


class MyTest(unittest.TestCase):
    
    def test_athlete_file_exist(self):
        print('\nTesting if athlete.csv file exists...')
        self.assertTrue(os.path.exists('athletes.csv'))
        print("PASS")
    
    def test_sport_events_file_exists(self):
        print('Testing if sport_events.csv file exists...')
        self.assertTrue(os.path.exists('sport_events.csv'))
        print("PASS")
    
    def test_with_1_rows(self):
        dataframe = pd.DataFrame([{0: '0', 'd': 50, 'finish_time_seconds': 5}])
        print('Testing column_velocity with 1 row...')
        self.assertEqual(column_velocity(dataframe),[300])
        print("PASS")

    def test_with_3_rows(self):
        dataframe = pd.DataFrame([{0: '0', 'd': 50, 'finish_time_seconds': 5},\
                                         {1: '1', 'd': 100, 'finish_time_seconds': 5},\
                                         {2: '2', 'd': 100, 'finish_time_seconds': 10}])
        print('Testing column_velocity with 3 rows...')
        self.assertEqual(column_velocity(dataframe),[300,300,150])
        print("PASS")

    
    def test_with_2_duplicate_columns_same_values(self):
        dataframe = pd.DataFrame([{0: '0', 'd': 50, 'finish_time_seconds': 5,'finish_time_seconds': 5},\
                                         {1: '1', 'd': 100, 'finish_time_seconds': 5, 'finish_time_seconds': 5},\
                                         {2: '2', 'd': 100, 'finish_time_seconds': 10, 'finish_time_seconds': 10}])
        print('Testing column_velocity result with duplicate columns with same values...')
        self.assertEqual(column_velocity(dataframe), [300,300,150])
        print("PASS")
        
    def test_with_2_duplicate_columns_different_values(self):
        dataframe = pd.DataFrame([{0: '0', 'd': 50, 'finish_time_seconds': 5,'finish_time_seconds': 5},\
                                         {1: '1', 'd': 100, 'finish_time_seconds': 5, 'finish_time_seconds': 10},\
                                         {2: '2', 'd': 100, 'finish_time_seconds': 10, 'finish_time_seconds': 10}])
        print('Testing column_velocity result with duplicate columns with different values...')
        self.assertEqual(column_velocity(dataframe), [300,150,150])
        print("PASS")
        
if __name__ == '__main__':
    unittest.main()

