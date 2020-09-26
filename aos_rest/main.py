"""
Main module of aos-rest scrapper.
"""
import json

from aos_rest.client import *


def main():
    get_court_divisions()


def get_court_divisions():
    cc = CommonCourtsClient()
    r = cc.get()

    courts = r.json()

    with open('../output/courts.json', 'w') as f:
        json.dump(courts, f, indent=4)

    divisions_list = []
    c = 0
    cdc = CourtDivisionClient()
    for court in courts:
        id = court['id']
        divisions = cdc.get_by_id(id).json()

        divisions_list.append({
            'court_id': id,
            'divisions': divisions
        })

    with open('../output/cc_divisions.json', 'w') as f:
        json.dump(divisions_list, f, indent=4)


if __name__ == '__main__':
    main()
