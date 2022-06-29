import pandas as pd
import numpy as np


class CsvReader:
    def __init__(self):
        self.array = None
        self.template = pd.read_csv('csv_header_template.csv', header=None).to_numpy()
        self.delete_nan()

    def delete_nan(self):
        cleaned_list = []
        for row in self.template:
            row = [x for x in row if str(x) != 'nan']
            cleaned_list.append(row)
        self.template = cleaned_list

    def open_csv(self, file):
        try:
            self.array = pd.read_csv(file)
        except Exception as exc:
            return exc

    def detect_file(self):
        if list(self.array) in self.template:
            if list(self.array) == self.template[0]:
                return 'pms'
            elif list(self.array) == self.template[1]:
                return 'wages'
        else:
            print('wrong file')

    def process_csv(self, file):
        self.open_csv(file)
        self.detect_file()
