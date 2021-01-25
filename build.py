import os

cd = os.path.join(os.path.dirname(os.getcwd()), "maven")  # Path ../maven


def buildIndex(path):
    if ".git" in path.replace(cd, ""):
        return

    head = open("./head.html", "r", encoding="UTF-8").read()
    body = open("./body.html", "r", encoding="UTF-8").read()
    head = head.replace("{{ title }}", path.replace(cd, "Index of ").replace("\\", "/"))
    body = body.replace("{{ name }}", path.replace(cd, "Index of ").replace("\\", "/"))
    body += '<ul>\n'
    if not path.__eq__(cd):
        body += '<li><a href="../">../</a><br/></li>\n'
    for file in os.listdir(path):
        if "index.html" not in file and not file.__eq__(".git"):
            body += '<li><a href="' + file + '">' + file + '</a></li>\n'
    body += '</ul>'
    template = open("./template.html", "r", encoding="UTF-8").read().replace("{{ head }}", head).replace(
        "{{ body }}", body)
    open(path + "/index.html", "w", encoding="UTF-8").write(template)


buildIndex(cd)

for root, dirs, files in os.walk(cd):
    for dir in dirs:
        buildIndex(os.path.join(root, dir))
