from gingerit.gingerit import GingerIt

def mark_incorrect_words(text):
    parser = GingerIt()
    result = parser.parse(text)
    corrected_text = result['result']

    # Create markup for all occurrences of incorrect words with '*' character
    incorrect_words = result['corrections']
    for correction in incorrect_words:
        incorrect_word = correction['text']
        corrected_word = f'*{incorrect_word}*'
        corrected_text = corrected_text.replace(incorrect_word, corrected_word)

    return corrected_text

if __name__ == "__main__":
    file_path = input("Enter the path of the .txt file to correct: ")

    try:
        with open(file_path, 'r') as file:
            original_content = file.read()
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
        exit()

    corrected_content = mark_incorrect_words(original_content)

    output_file = file_path.replace(".txt", "_marked.txt")
    try:
        with open(output_file, 'w') as file:
            file.write(corrected_content)
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
        exit()

    print("Grammar and spelling correction done successfully. New file with incorrect word marks saved.")
