from gingerit.gingerit import GingerIt

def correct_grammar(text):
    parser = GingerIt()
    result = parser.parse(text)
    corrected_text = result['result']
    return corrected_text

if __name__ == "__main__":
    file_path = input("Enter the path of the .txt file to correct: ")
    
    try:
        with open(file_path, 'r') as file:
            original_content = file.read()
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
        exit()

    corrected_content = correct_grammar(original_content)

    try:
        with open(file_path, 'w') as file:
            file.write(corrected_content)
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
        exit()

    print("Grammar and spelling correction done successfully.")
