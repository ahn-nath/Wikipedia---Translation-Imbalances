# test the functions in the file: utils.py

import unittest
import utils


class Test(unittest.TestCase):
    # test clean_data_and_update_rows
    def test_clean_data_and_update_rows(self):
        # initial input
        allowed_langs = ['fr', 'en', 'de', 'hi', 'bn', 'mr', 'cs', 'sk']
        sample_data = {'Olivier LPB': {'username': 'Olivier LPB',
                                       'language': "['fr-5', 'en-2']",
                                       'edit_counts': [],
                                       'level_lang': []},
                       'Gamesmasterg9': {'username': 'Gamesmasterg9',
                                         'language': "['en-5', 'hi-4', 'bn-3', 'mr-1']",
                                         'edit_counts': [],
                                         'level_lang': []},
                       'Dvermeirre': {'username': 'Dvermeirre',
                                      'language': "['fr-5', 'en-5', 'de-1']",
                                      'edit_counts': [],
                                      'level_lang': []},
                       'Jklamo': {'username': 'Jklamo',
                                  'language': "['en-3', 'cs-5', 'sk-5', 'fr-1']",
                                  'edit_counts': [],
                                  'level_lang': []}}

        # expected output
        expected_user_dictionary = {'Olivier LPB': {'username': 'Olivier LPB',
                                                    'edit_counts': {'fr': 0, 'en': 0},
                                                    'level_lang': [('fr', '5'), ('en', '2')]},
                                    'Gamesmasterg9': {'username': 'Gamesmasterg9',
                                                      'edit_counts': {'en': 0, 'hi': 0, 'bn': 0, 'mr': 0},
                                                      'level_lang': [('en', '5'), ('hi', '4'), ('bn', '3'),
                                                                     ('mr', '1')]},
                                    'Dvermeirre': {'username': 'Dvermeirre',
                                                   'edit_counts': {'fr': 0, 'en': 0, 'de': 0},
                                                   'level_lang': [('fr', '5'), ('en', '5'), ('de', '1')]},
                                    'Jklamo': {'username': 'Jklamo',
                                               'edit_counts': {'en': 0, 'cs': 0, 'sk': 0, 'fr': 0},
                                               'level_lang': [('en', '3'), ('cs', '5'), ('sk', '5'), ('fr', '1')]}}

        expected_language_match_dictionary = {'fr': ['Olivier LPB', 'Dvermeirre', 'Jklamo'],
                                              'en': ['Olivier LPB', 'Gamesmasterg9', 'Dvermeirre', 'Jklamo'],
                                              'hi': ['Gamesmasterg9'],
                                              'bn': ['Gamesmasterg9'],
                                              'mr': ['Gamesmasterg9'],
                                              'de': ['Dvermeirre'],
                                              'cs': ['Jklamo'],
                                              'sk': ['Jklamo']}

        # assert
        self.assertEqual(utils.clean_data_and_update_rows(sample_data, allowed_langs),
                         (expected_user_dictionary, expected_language_match_dictionary))
