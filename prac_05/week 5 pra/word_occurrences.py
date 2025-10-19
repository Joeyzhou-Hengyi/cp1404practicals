def main():
    text = input("Text: ").strip()
    words = text.lower().split()
    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    # Find the longest word
    if len(counts) > 0:
        longest = max(len(word) for word in counts)
    else:
        longest = 0

    for word in sorted(counts):
        print(f"{word:{longest}} : {counts[word]}")


if __name__ == "__main__":
    main()