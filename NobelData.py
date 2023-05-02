# Author: Justin Huang
# GitHub username: huangjus
# Date: 5/2/23
# Description: The code has a private data member _data, which stores the Nobel Prize data read from the JSON file.
# The __init__ method initializes this data member by reading the JSON file using the json module.
# The search_nobel method takes a year and category as input, searches the prize data for winners in the given year
# and category, and returns a sorted list of their surnames.

import json


class NobelData:
    def __init__(self, filename='nobels.json'):
        """
        Reads a JSON file containing Nobel Prize data and stores it in a private data member.
        """

        with open(filename, 'r') as infile:
            self._data = json.load(infile)

    def search_nobel(self, year, category):
        """
        Searches the Nobel Prize data for winners in the given year and category, and returns a sorted list of their
        surnames.
        """
        
        laureates = []
        for prize in self._data['prizes']:
            if prize['year'] == year and prize['category'].lower() == category.lower():
                for laureate in prize['laureates']:
                    if 'surname' in laureate:
                        laureates.append(laureate['surname'])
        return sorted(laureates)
