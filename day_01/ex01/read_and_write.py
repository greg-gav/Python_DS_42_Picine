def piece_of(line: str):
    if line[0] == '"':
        ind = line[1:].find('"')
        yield line[ind + 3:]
    else:
        ind = line.find(",")
        yield line[ind + 1:]


def read_and_replace():
    with open("ds.csv", "r") as in_file:
        file = in_file.readlines()
    out_file = open("ds.tsv", "w")
    for line in file:
        outline = ""
        saved = line
        while line := next(piece_of(line)):
            outline += f"{saved[:len(saved)-len(line)].strip(',')}\t"
            saved = line
        outline += f"{saved[:len(saved)-len(line)].strip(',')}\t"
        out_file.write(f"{outline.strip()}\n")
    out_file.close()


if __name__ == "__main__":
    read_and_replace()
