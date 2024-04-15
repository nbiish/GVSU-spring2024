while True:
    text = input()
    if text.lower() in ['done', 'd']:
        break
    print(text[::-1])