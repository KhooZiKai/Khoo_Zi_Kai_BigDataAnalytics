import csv
import re

def clean_text(text):
    # Define the characters to be removed
    characters_to_remove = r'",.[]{}\/|\\-()#$%^&*!@~?><:;=+'

    # Use regular expression to remove the characters
    cleaned_text = re.sub(f'[{re.escape(characters_to_remove)}]', '', text)
    return cleaned_text

def clean_csv(input_file, output_file):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            cleaned_row = [clean_text(cell) for cell in row]
            writer.writerow(cleaned_row)

if __name__ == '__main__':
    input_csv_file = r"C:\Users\khooz\Downloads\NER_split\NER_only.csv"  # Only Works On My Computer, Change to you Input Path
    output_csv_file = r"C:\Users\khooz\Downloads\NER_split\NER_clean.csv"  # Only Works On My Computer, Change to you Output Path

    clean_csv(input_csv_file, output_csv_file)


