def parse_jawiki_json(filename = "jawiki-country.json"):
    with open("jawiki-country.json") as f:
        jawiki = f.readlines()

    jawiki_oneline = []
    for line in jawiki:
        jawiki_oneline.append(line.split(":")[1])

    jawiki_body = []
    for line in jawiki_oneline:
        jawiki_body.append(line.split("\\n"))

    print (jawiki_body[0])
if __name__ == "__main__":
    parse_jawiki_json()
