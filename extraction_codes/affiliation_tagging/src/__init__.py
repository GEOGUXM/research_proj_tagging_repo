from src.affiliation_operations import affiliation_operations
folder_path = r"C:\Users\temp\Desktop\research_proj_tagging_repo\affiliation_tagging_files\raw_files2"
# folder_path = r"C:\Users\temp\Desktop\Targets"
reference_path = r"C:\Users\temp\Desktop\research_proj_tagging_repo\affiliation_tagging_files\matches.txt"

ao = affiliation_operations(folder_path, reference_path)
# ao = affiliation_operations(folder_path)
ao.readTaggedAffiliationFiles()
ao.fileIterator()