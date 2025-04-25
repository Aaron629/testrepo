def countnum():
    while True:
        try:
            num = input("Enter num: ")
            if not num:
                break
            count = len(num.split())
            print(f"Word count: {count}")
        except EOFError:
            break