def counttext():
    while True:
        try:
            text = input("Enter text: ")
            if not text:
                break
            count = len(text.split())
            print(f"Word count: {count}")
        except EOFError:
            break