import os
import sys
import datetime


def create_file() -> None:
    file_name = None
    dir_parts = []

    args = sys.argv[1:]
    i = 0

    while i < len(args):
        if args[i] == "-f":
            file_name = args[i + 1]
            i += 2

        elif args[i] == "-d":
            i += 1
            while i < len(args) and args[i] not in ("-f", "-d"):
                dir_parts.append(args[i])
                i += 1
        else:
            i += 1

    if dir_parts:
        dir_path = os.path.join(*dir_parts)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = ""

    if file_name:
        file_path = os.path.join(
            dir_path,
            file_name
        ) if dir_path else file_name
        write_content(file_path)


def write_content(file_path: str) -> None:
    with open(file_path, "a") as new_file:
        if os.path.getsize(file_path) != 0:
            new_file.write("\n")

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_file.write(timestamp + "\n")

        counter = 1
        while True:
            text = input("Enter content line: ")

            if not text or text.lower() == "stop":
                break

            new_file.write(f"{counter} {text}\n")
            counter += 1
