import csv

def format_bullet_points(text):
    if '*' in text:
        # Split the text at the first '*' and separate the initial text from the bullet points
        first_part, bullet_points_part = text.split('*', 1)
        # Split the remaining text into bullet points
        bullet_points = bullet_points_part.split('*')
        # Create an HTML unordered list for the bullet points
        formatted_bullet_points = '<ul>' + ''.join(f'<li>{item.strip()}</li>' for item in bullet_points if item.strip()) + '</ul>'
        return first_part + formatted_bullet_points
    else:
        return text

def csv_to_anki_with_bullets(csv_file_path, anki_file_path):
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        with open(anki_file_path, 'w', encoding='utf-8') as anki_file:
            for row in csv_reader:
                question, answer, tags = row[0], row[1], row[2]
                formatted_answer = format_bullet_points(answer)
                anki_file.write(f"{question}\t{formatted_answer}\t{tags}\n")

# Usage
csv_file_path = 'input.csv'  # Replace with your CSV file path
anki_file_path = 'output/output.txt'  # Replace with your desired output file path
csv_to_anki_with_bullets(csv_file_path, anki_file_path)
