import requests

build_req = requests.get("https://papermc.io/api/v2/projects/travertine/")
build = build_req.json()['version_groups'][-1]

builds_req = requests.get("https://papermc.io/api/v2/projects/paper/version_group/{}/builds".format(build))
recent = builds_req.json()

version = recent['versions'][-1]
recent = recent['builds'][-1]
build_number = recent['build']
jar = recent['downloads']['application']['name']

string = "https://papermc.io/api/v2/projects/paper/versions/{version}/builds/{build}/downloads/{jar}".format(
    version=version,
    build=build_number,
    jar=jar
)

print(string)

