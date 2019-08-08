import os, json

# read all json file located in dir: src_path
# find the ones with author tag: "contain_publication_list": "T"
# copy those json contents to separate files, in the same folder: res_path
# attach ref file to all extracted files: matches.txt

src_path = r"C:\Users\temp\Desktop\data\a\49\5001\38026c9f-3abd-491d-9500-2add55ea1ae7.html"

path = os.listdir(src_path)
print(path)