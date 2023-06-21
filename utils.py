## Clean initial data and update rows and prepare data for requests
import ast
import re
from collections import defaultdict


def clean_data_and_update_rows(user_dictionary, allowed_languages):
    """
    Clean data and update rows
    :param allowed_languages:
    :param user_dictionary: raw data
    :return: cleaned data and updated rows; dictionary needed to make request by language and associated user list.
    """

    # dictionary needed to make request by language and associated user list
    language_match_dict = defaultdict(list)

    for key, row in user_dictionary.items():
        username = row['username']
        languages = ast.literal_eval(row['language'])
        level_lang = []
        edit_keys = []

        for lang in languages:
            # split by digits with a preceding character ('-') and include it
            lang_extract = list(filter(None, re.split('-(\d)|-[A-Z]+', lang)))
            # get the language
            lang = lang_extract[0]
            # get language level if present, else, assume native level
            level = lang_extract[1] if len(lang_extract) > 1 else 5

            if (lang in allowed_languages) and (lang not in edit_keys):
                # append
                level_lang.append((lang, level))
                # initialize key
                edit_keys.append(lang)

                # add to the user to the corresponding language group
                language_match_dict[lang].append(username)

        # update row columns after cleaning
        row['level_lang'] = level_lang
        # we are creating a dictionary to easily map and update by user and language after
        # getting the raw counts. We initialize to 0 to only update data that is not 'missing'
        row['edit_counts'] = dict.fromkeys(edit_keys, 0)
        # 'unset' language
        del row['language']

    return user_dictionary, language_match_dict
