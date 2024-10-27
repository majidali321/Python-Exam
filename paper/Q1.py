def analyze_file(sample):
   
    try:
        with open(sample, 'r') as file:
            lines = file.readlines()
            characters = sum(len(line) for line in lines)
            words = sum(len(line.split()) for line in lines) 
            line_count = len(lines) 

            return {
                'characters': characters,
                'words': words,
                'lines': line_count
            }
    except FileNotFoundError:
        print(f"file '{sample}' is not found.")
        return None
    except Exception as f:
        print(f"Error : {f}")
        return None

def search_word(sample, word):  #example
    try:
        count = 0
        with open(sample, 'r') as file:
            for line in file:
                count += line.lower().split().count(word.lower()) 
        return count
    except FileNotFoundError:
        print(f"sorry: The file '{sample}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


result = analyze_file('sample.txt')
if result:
    print("File Analysis:", result)


wordCount = search_word('sample.txt', 'SMIT')
if wordCount is not None:
    print(f"The word 'SMIT' appears {wordCount} times in the file.")
