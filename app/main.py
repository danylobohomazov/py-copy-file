def copy_file(command: str) -> None:
    if len(command.split()) != 3:
        return
    cp, file_name1, file_name2 = command.split()
    if (file_name1 == file_name2
            or ".txt" not in file_name1
            or ".txt" not in file_name2
            or cp != "cp"):
        return
    try:
        with open(file_name1, "r") as file, open(file_name2, "w") as copy:
            for line in file:
                copy.write(line)
    except FileNotFoundError:
        return
