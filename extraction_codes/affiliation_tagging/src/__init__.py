from src.affiliation_operations import affiliation_operations
folder_path = r"C:\Users\temp\OneDrive\Research Project\raw_files2"
reference_path = r"C:\Users\temp\Desktop\process_res\matches.txt"

ao = affiliation_operations(folder_path, reference_path)
ao.readTaggedAffiliationFiles()
ao.fileIterator()