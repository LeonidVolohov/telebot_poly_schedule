import requests
import json


def get_groups(api_link: str) -> dict:
    '''Gets all available groups and creates a dict of group_ids and faculty_ids'''
    link = api_link + '/faculties'
    faculties = json.loads(requests.get(link).text)
    # group_number: (faculty_id, group_id)
    group_ids = {}
    for faculty in faculties['faculties']:
        got = False
        id = faculty['id']
        while not got:
            try:
                groups = json.loads(requests.get(link + '/' + str(id) + '/groups', timeout=2).text)
                got = True
            # If API server doesn't respond or responds with corrupted json
            except:
                print('attempt to get groups of ' + faculty['name'] + ' failed. Retrying...')
        for group in groups['groups']:
            group_ids[group['name']] = (faculty['id'], group['id'])
    return group_ids


if __name__ == "__main__":
    get_groups('http://ruz.spbstu.ru/api/v1/ruz')
