import time

def typing_test():
    text = "Hacktoberfest is a celebration of open-source contributions."
    print("\n Type this sentence:\n")
    print(f">>> {text}\n")

    input("Press Enter to start...")
    start = time.time()
    typed = input("\nStart typing: ")
    end = time.time()

    elapsed = end - start
    words = len(typed.split())
    wpm = (words / elapsed) * 60

    print(f"\n Time: {round(elapsed, 2)} sec")
    print(f"Speed: {round(wpm, 2)} WPM")
    print("Match!" if typed.strip() == text else "Text does not match.")

if __name__ == "__main__":
    typing_test()
