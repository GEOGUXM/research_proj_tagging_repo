import os, json

# read all json file located in dir: src_path
# find the ones with author tag: "contain_publication_list": "T"
# copy those json contents to separate files, in the same folder: res_path
# attach ref file to all extracted files: matches.txt

# project globals
SRC_PATH = r"C:\Users\temp\Desktop\data"
DEST_PATH = r"C:\Users\temp\Desktop\Targets2"

# collect all json files paths
json_files = []
for item in os.walk(SRC_PATH):
    if item[1] == ['pub'] and item[2] != []:
        for file in item[2]:
            if ".json" in file:
                json_files.append(item[0] + "\\" + file)

# open json file one by one, testing on "contain_publication_list" is T or F
target_files = []
for json_file in json_files:
    fp = open(json_file, "r")
    json_content = json.loads(fp.read())
    fp.close()
    if json_content["contain_publication_list"] == "T":
        target_files.append(json_file.split(".tag.json")[0] + ".txt")

# copy all target files from raw data
for src_file in target_files:
    file_name = src_file.split("\\")[-1]
    wt = open(DEST_PATH + "\\" + file_name, "w+")
    # write tagging headers
    wt.writelines("###OriginPath=" + src_file + "\n")
    wt.writelines("###AuthorName=\n")
    wt.writelines("###AuthorTitle=\n")
    wt.writelines("###Affiliation=\n")
    wt.writelines("###Position=\n")
    wt.writelines("##############################\n")
    # write remaining contents
    rd = open(src_file, "r")
    wt.write(rd.read())
    rd.close()
    wt.close()

for item in target_files:
    print(item)

print(len(target_files))