words = input("> ").split(" ")    # This separates the words by ' '

emoji_mapping = {
    ":)":"😊",
    ":(":"😢",
    ":|":"🤐",
    "cool":"😎"
}
output = ""
for word in words:
    output += emoji_mapping.get(word, word)+ " "
print(output)

