# read data in RESULT.txt tagging file
# insert tagged data into raw folders respectively

import json
from ast import literal_eval as make_tuple

result_path = r"C:\Users\temp\Desktop\data\RESULT.txt"
# folder_path = r"C:\Users\temp\Desktop\data"

# read all valid lines in RESULT.txt file
all_results = []
fp = open(result_path, "r")
for line in fp.readlines():
    if not line.split("###")[1].strip() == "(N=||Y=||T=||V=)":
        all_results.append((make_tuple(line.split("###")[0]), line.split("###")[1].strip()[1:-1]))
    else:
        break
fp.close()

#read out source file path for each tagged pub item
pre_path = ""
fp = None
all_json = {}

for res in all_results:
    res_path = res[0][0]
    res_index = int(res[0][2][2])
    res_tags = res[1].split("||")

    if res_path == pre_path:
        # just write
        for pub in all_json["publications"]:
            pub_index = pub["start_index_in_file"]
            # if index matching
            if pub_index == res_index:
                for res_tag in res_tags:
                    tag, text = res_tag.split("=")
                    if tag == "N":
                        pub["authors"] = text
                    elif tag == "Y":
                        pub["year"] = text
                    elif tag == "T":
                        pub["title"] = text
                    elif tag == "V":
                        pub["venue"] = text
                break
    else:
        # write previous result to json files
        if all_json != {} and pre_path != "":
            all_write = json.dumps(all_json)
            # print(all_write)
            fp = open(pre_path, "w+")
            fp.write(all_write)
            fp.close()
        # read new json file corresponding to current pub
        fp = open(res_path, "r")
        all_json = json.loads(fp.read())
        fp.close()
        fp = None
        # then insert to publication tag, id = start_char_index
        for pub in all_json["publications"]:
            pub_index = pub["start_index_in_file"]
            # if index matching
            if pub_index == res_index:
                for res_tag in res_tags:
                    tag, text = res_tag.split("=")
                    if tag == "N":
                        pub["authors"] = text
                    elif tag == "Y":
                        pub["year"] = text
                    elif tag == "T":
                        pub["title"] = text
                    elif tag == "V":
                        pub["venue"] = text
                break

    pre_path = res_path


