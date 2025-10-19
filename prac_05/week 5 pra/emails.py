def extract_name_from_email(address):
    local_part = address.split("@")[0]
    parts = local_part.replace(".", " ").replace("_", " ").replace("-", " ").split()
    name = " ".join(parts).title()
    return name if name != "" else local_part.title()


def main():
    email_to_name = {}

    user_email = input("Email: ").strip()
    while user_email != "":
        guessed_name = extract_name_from_email(user_email)
        confirmation = input(f"Is your name {guessed_name}? (Y/n) ").strip().lower()
        if confirmation not in ("", "y"):
            guessed_name = input("Name: ").strip().title()

        email_to_name[user_email] = guessed_name
        user_email = input("Email: ").strip()

    print()
    for e, n in email_to_name.items():
        print(f"{n} ({e})")

main()