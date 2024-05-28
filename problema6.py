def lungimeString():
    try:
        text=input("Introduceti text:")
        lungime=len(text)
        print(f"Lungimea stringului este: {lungime}")
    except ValueError as e:
        print(e)
print("test")
lungimeString()