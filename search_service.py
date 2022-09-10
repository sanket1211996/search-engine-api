import csv


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

    def filterData(self, search_text):
        print('Search String' + search_text)
        jsonArray = self.csv_to_json('data.csv')
        return jsonArray
