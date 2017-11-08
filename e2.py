import requests

addr = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/"
resp = requests.get(addr)

for line in open("ELECTION_ID"):
    file_name = year +".csv"

with open(file_name, "w") at out:
        out.write(resp.text)
