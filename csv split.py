import csv


def extract_ner_column(input_file, output_file):
    with open (input_file, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)  # Delete First Row Header
        ner_index = header.index('NER')

        with open(output_file, 'w', newline='', encoding='utf-8') as out_file:
            csv_writer = csv.writer(out_file)
            csv_writer.writerow(['NER'])  # New Header

            for row in csv_reader:
                ner_value = row[ner_index]
                csv_writer.writerow([ner_value])


if __name__ == "__main__":
    input_file = r"C:\Users\khooz\Downloads\Recipes\recipes_data.csv"  # Only Works On My Computer, Change to you Input Path
    output_file = r"C:\Users\khooz\Downloads\NER_split\NER_only.csv"  # Only Works On My Computer, Change to you Output Path