NAME_TO_HEX = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blueviolet": "#8a2be2",
    "coral": "#ff7f50",
}


def main():
    colour_name = input("Colour name (blank to quit): ").strip()
    while colour_name != "":
        key = colour_name.lower()
        try:
            print(f"{colour_name} -> {NAME_TO_HEX[key]}")
        except KeyError:
            print("Invalid colour name")
        colour_name = input("Colour name (blank to quit): ").strip()

main()