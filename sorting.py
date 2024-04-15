import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    data = {}
    with open(file_path, mode='r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        # Přičtení hlavičky
        headers = next(csv_reader)

        # Inicializacee - Pro každý sloupec - prázdný seznam v datovém slovníku
        for header in headers:
            data[header] = []

        # Načtení dat ze zbývajících řádků csv souboru
        for row in csv_reader:
            # Přidání čísel z řádku do odpovídajícího seznamu
            for i, value in enumerate(row):
                data[headers[i]].append(float(value))
        return data


def selection_sort(data):
    print(data)
#    for nazev, seznam in data:

    return


def main():
    # Nazev csv souboru
    filename = 'numbers.csv'
    data = read_data(filename)
#    print(data)
    print(selection_sort(data))


if __name__ == '__main__':
    main()
