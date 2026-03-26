import random

def generate_line(base_string, length, len_to_use = 27):
    base_string = base_string[:len_to_use]
    letters = {}
    for l in base_string:
        for letter in l:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    
    letters = dict(sorted(letters.items(), key=lambda item: item[1], reverse=True))
    probability_of_letters = {}
    for letter in letters:
        probability_of_letters[letter] = letters[letter] / len(base_string)
    return random.choices(list(probability_of_letters.keys()), list(probability_of_letters.values()), k=length)

def show_line_stats(line):  
    words = line.split()
    print("Number of words:", len(words))
    length_of_words = 0
    for word in words:
        length_of_words += len(word)
    print(f"Summary length of words: {length_of_words}")
    print(f"Average length of words: {length_of_words / len(words)}\n")

def main():
    # generator przyblizenia zerowego rzedu
    random_line = generate_line('abcdefghijklmnopqrstuvwxyz ', 50, 27)
    print("Generated line:", "".join(random_line))
    show_line_stats("".join(random_line))

    with open("data/norm_wiki_sample.txt", "r") as f:
        line = f.readline()

    # przyblizenie pierwszego rzedu
    random_line = generate_line(line, 50, 20000)
    print("Generated line:", "".join(random_line))
    show_line_stats("".join(random_line))

    show_line_stats(line)
if __name__ == "__main__":
    main()