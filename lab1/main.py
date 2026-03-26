import random

# with open("data/norm_romeo.txt", "r") as f:
#     lines = f.readlines()

# print("Lines in the file: ", len(lines))
# print(lines)
def generate_line(length):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"," "]
    line = ""
    for i in range(length):
        line += random.choice(letters)
    return line

def show_line_stats(line):  
    words = line.split()
    print("Number of words:", len(words))
    length_of_words = 0
    for word in words:
        length_of_words += len(word)
    print("Length of each word:", length_of_words)
    print("Average length of words:", length_of_words / len(words))

def main():
    #generator przyblizenia zerowego rzedu
    # random_line = generate_line(50)
    # print("Random line:", random_line)
    # show_line_stats(random_line)
    with open("data/norm_wiki_sample.txt", "r") as f:
        line = f.readline()

    print("Lines in the file: ", len(line))
    print(line)
    # lines = line.split()

    letters = {}
    for l in line:
        for letter in l:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    
    letters = dict(sorted(letters.items(), key=lambda item: item[1], reverse=True))
    print("Letters in the file:", len(line))
    probability_of_letters = {}
    for letter in letters:
        probability_of_letters[letter] = letters[letter] / len(line)

    
    
    print(letters)
    print(probability_of_letters)

    x=random.choices(list(probability_of_letters.keys()), list(probability_of_letters.values()), k=50)
    print("Random line:", "".join(x))




if __name__ == "__main__":
    main()