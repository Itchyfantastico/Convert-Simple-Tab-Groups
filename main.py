import json

output = []

f = open("<your backup file>.json", encoding="utf8")
data = json.load(f)
f.close()

for group in data["groups"]:
    output.append("## " + group["title"])
    for tab in group["tabs"]:
        output.append(tab["url"])

    output.append("")

f = open("tab stash input.txt", "x")
for line in output:
    f.write(line + "\n")
f.close()
