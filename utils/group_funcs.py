import sys
sys.path.insert(1, '/*MyPath*/code/utils/')

import schedule_funcs

USER_GROUPS = {}  # stores group number for each user
GROUP_IDS = {}  # group_number: (faculty_id, group_id). Add Possible groups here


def parse_group_from_user(message_text: str) -> int:
    '''Gets user message and tries to extract group number info from it.
    If successful - returns corresponding tuple (faculty_id, group_id).
    Otherwise raises ValueError'''
    message_as_list = message_text.split()
    if len(message_as_list) != 2:
        raise SyntaxError

    # group_number is a string
    group_number = message_as_list[1]

    # Check if group with such number exists at all
    if group_number not in GROUP_IDS.keys():
        raise ValueError

    return group_number


def remember_relation(user_id: int, group: str):
    '''Adds user-group relation and creates a schedule if needed'''
    USER_GROUPS[user_id] = group
    schedule_funcs.update_schedule_list(GROUP_IDS[group][1])
