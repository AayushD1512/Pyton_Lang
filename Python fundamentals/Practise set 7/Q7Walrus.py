# while (txt := input("Enter something: ")) not in ("quit", "Quit", "QUIT"):
#     print(f"You entered this text: {txt}")


word = ["python", "java", "c++", "javascript", "html", "css"]

# lengths = [n for w in word if (n:= len(w))>=4]
# word_pairs = [(w, len(w)) for w in word if len(w) >= 4]
onlyWord = [w for w in word if len(w) >4]
print(onlyWord)