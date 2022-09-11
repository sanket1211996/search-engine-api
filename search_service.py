import csv
from os.path import exists

from fuzzywuzzy import fuzz
# from fuzzywuzzy import process
import pandas as pd
from securities import Securities


class SearchService:

    def csv_to_json(self, csvFilePath):
        jsonArray = []

        # read csv file
        with open(csvFilePath, encoding='utf-8') as csvf:
            # load csv file data using csv library's dictionary reader
            csvReader = csv.DictReader(csvf)

            # convert each csv row into python dict
            for row in csvReader:
                # add this python dict to json array
                jsonArray.append(row)

        return jsonArray

    # csvFilePath = r'data.csv'
    # # jsonFilePath = r'data.json'
    # csv_to_json(csvFilePath)

    def search(self, searchText, df):

        found_index = []
        for index in range(len(df)):

            if df.text.iloc[index] is not None:  # modified
                score = fuzz.partial_ratio(searchText, df.text.iloc[index])
                # print(score)
                if score > 90:
                    # print(score)
                    found_index.append(index)

        print('found data', len(found_index))
        priority = [9, 4, 10, 5, 3, 7, 1, 2, 0, 6, 8, 9999]

        priorityDF = []
        for index in found_index:
            priorityDF.append(df.text.iloc[index].split(' '))
        # priorityDF[0][-1] = 0
        # print(priorityDF[0])
        for index in range(len(priorityDF)):
            current_row = priorityDF[index]
            # print('currentRow', currentRow)
            MINI = 9999
            found = False
            for col in range(len(current_row)):
                if searchText in current_row[col]:
                    found = True
                    # print('INDEX', col)
                    MINI = min(MINI, priority[col])
            if found:
                priorityDF[index].append(MINI)

        priorityDF = [tuple(z) for z in priorityDF]
        priorityDF.sort(key=lambda x: x[-1])
        # for row in priorityDF:
        #     print(row)
        return priorityDF

    def filterData(self, search_text):
        print('Search String: ' + search_text)
        resultJson = []
        if exists('./data/mini_pickle'):
            df = pd.read_pickle('./data/mini_pickle')
            searchdata = self.search(search_text, df)

            for row in searchdata:
                if len(row) == 12:
                    resultJson.append(
                        Securities(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                   row[10], row[11]))
        else:
            print('Pickle not found')

        # jsonArray = self.csv_to_json('data.csv')
        # if search_text == '1':
        #     return [jsonArray[0]]
        return resultJson

# ss = SearchService()
# print(ss.filterData('B'))
