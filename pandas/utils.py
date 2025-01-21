import csv
import pandas as pd
import sys

maxInt = sys.maxsize
while True:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

def read_csv_as_dataframe(infile_path):
    # Create an empty list to store rows
    data_rows = []

    # Read in the data from the CSV file
    with open(infile_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        # read the header
        header = next(reader)
        header_count = len(header)
        try:
            while data := next(reader):
                data_count = len(data)
                flag = False
                while data_count != header_count:
                    data_next = next(reader, None)
                    if data_next is None:
                        break
                    if len(data_next) == 0:
                        data_next = next(reader, None)
                        if data_next is None:
                            break
                    data[-1] = data[-1] + data_next[0]
                    data = data + data_next[1:]
                    data_count = len(data)
                    if data_count != header_count:
                        flag = True
#                        print(f'Detected ((data_count != header_count) ): {data}')
                # Remove newline characters from each item in data
                data = [item.replace('\n', '') for item in data]
                if flag:
#                    print(f'>After correction: {data}')
                    flag = False
                # Append data to the list instead of DataFrame
                data_rows.append(data)
        except StopIteration:
            print(f'End of file reached: {infile_path}')

        # Convert the list to a DataFrame
        df = pd.DataFrame(data_rows, columns=header)

        return df