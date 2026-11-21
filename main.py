"""Write one short relaxing text for the make.fun AI judge.

The text (268 characters) is a quiet night scene: a still house, an enormous
starry sky, and the reassurance that nothing is asking anything of the reader.
"""

import os

TEXT = (
    "The kettle has gone quiet and the house is still. Outside, the night is "
    "enormous, stars packed so thick above the rooftops that the dark between "
    "them feels thin. You are very small under all of that, and nothing here "
    "is asking anything of you. The next page will wait."
)

assert 1 <= len(TEXT) <= 280
assert TEXT.strip()

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
