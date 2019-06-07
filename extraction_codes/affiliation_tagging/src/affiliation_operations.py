import os
import json

class affiliation_operations:
    folder_path = None
    reference_path = None
    file_paths = []
    all_refs = []

    def __init__(self, folder_path, reference_path):
        self.folder_path = folder_path
        self.reference_path = reference_path


    def readTaggedAffiliationFiles(self):
        # load file paths
        if self.folder_path != None:
            self.file_paths = []
            for file_name in os.listdir(self.folder_path):
                self.file_paths.append((self.folder_path + "\\" + file_name, file_name))
        # load reference file: mappings
        # print(self.reference_path)
        if self.reference_path != None:
            fp = open(self.reference_path, "r")
            self.all_refs = []
            for item in fp.read().split("\n"):
                if item != "":
                    self.all_refs.append(item.split("###")[0])
            fp.close()

    def getFilePath(self, file_name):
        for item in self.all_refs:
            if file_name in item:
                return item
        return None

    def fileIterator(self):
        if self.file_paths != []:
            for file_path, file_name in self.file_paths:
                self.processSingleFile(file_path, file_name)

    def processSingleFile(self, file_path, file_name):
        fp = open(file_path, "r")
        all_contents = fp.read()
        all_content_segs = all_contents.split("\n")
        fp.close()
        # fields to hold values for each file
        author_name = ""
        author_title = ""
        affiliation = ""
        position = ""
        line_cnt = 0
        for line in all_content_segs:
            if line.startswith("###AuthorName"):
                author_name = line.split("=")[1]
            elif line.startswith("###AuthorTitle"):
                author_title = line.split("=")[1]
            elif line.startswith("###Affiliation"):
                affiliation = line.split("=")[1]
            elif line.startswith("###Position"):
                position = line.split("=")[1]
            elif line.startswith("##############################"):
                line_cnt = 0
            else:
                # main text body
                # search for each field at the same time
                line_cnt += 1
                if author_name.strip() != "" and author_name in line.strip():
                    author_name = author_name + "%" + str(line_cnt)
                if author_title.strip() != "" and author_title in line.strip():
                    author_title = author_title + "%" + str(line_cnt)
                if affiliation.strip() != "" and affiliation in line.strip():
                    affiliation = affiliation + "%" + str(line_cnt)
                if position.strip() != "" and position in line.strip():
                    position = position + "%" + str(line_cnt)
        # parsing path
        src_file_path = self.getFilePath(file_name)
        # change file to json
        json_file_path = src_file_path.split(".")[0] + ".tag.json"
        # print(json_file_path)

        try:
            fp = open(json_file_path, "r")
        except:
            return
        all_json = json.loads(fp.read())
        fp.close()

        aff_contents = {}
        aff_contents["affiliation_info"] = []
        if author_title.strip() != "" and "%" in author_title.strip():
            temp_title = author_title.strip().split("%")[0]
            temp_line = author_title.strip().split("%")[1]
            aff_contents["affiliation_info"].append({"author_title": {"line_num":  int(temp_line), "text": temp_title}})
            
        if affiliation.strip() != "" and "%" in affiliation.strip():
            temp_affiliation = affiliation.strip().split("%")[0]
            temp_line = affiliation.strip().split("%")[1]
            aff_contents["affiliation_info"].append({"affiliation": {"line_num":  int(temp_line), "text": temp_affiliation}})

        if position.strip() != "" and "%" in position.strip():
            temp_position = position.strip().split("%")[0]
            temp_line = position.strip().split("%")[1]
            aff_contents["affiliation_info"].append({"position": {"line_num":  int(temp_line), "text": temp_position}})

        # write to origin file
        all_json.update(aff_contents)
        res = json.dumps(all_json)

        fp = open(json_file_path, "w+")
        fp.write(res)
        fp.close()
