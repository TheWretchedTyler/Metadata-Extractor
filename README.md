# Metadata-Extractor
It does just that, It extracts metadata from a file

Enhanced File Metadata Extractor

This is a Python tool that allows you to extract metadata from files and export it in either CSV or JSON formats. The tool supports multiple files and includes the option to check file integrity based on a known hash value. The metadata extraction includes information such as file name, size, creation time, modification time, access time, and SHA256 hash. It is my hope that this can be expanded into something much larger, with more tools readily avaliable to make comparison of data much easier for the analyst. I am also completely open to new ideas as I feel that this is a project that has unlimited manuverability and can be shaped in infinitely different ways.

Features:
Multiple file support: Select and extract metadata from multiple files.
File Integrity Check: Verify file integrity by comparing the file’s hash against a known hash (optional).
Export metadata: Export extracted metadata in either CSV or JSON formats.
User-friendly GUI: Simple interface built using Tkinter.
Requirements:
Python 3.x
tkinter (part of Python’s standard library)
hashlib (part of Python’s standard library)
csv and json (part of Python’s standard library)


Use the GUI:

Select Files: Click the "Browse" button to select one or more files for metadata extraction. You can select multiple files by holding Ctrl (Windows) or Cmd (Mac) while selecting.
Integrity Check: Optionally, enter a known hash in the provided field to check the integrity of the selected files.
Extract Metadata: Click the "Extract Metadata" button to begin the extraction process. The metadata will be displayed in the text box.
Export Metadata: After extraction, click "Export Metadata" to save the metadata in either CSV or JSON format.
Extracted Metadata:
For each file, the following metadata will be extracted:

File Name: The name of the file.
File Path: The full path to the file.
File Extension: The file’s extension (e.g., .txt, .jpg).
File Size: The size of the file, in human-readable format (e.g., KB, MB).
Creation Time: The timestamp when the file was created.
Last Modified Time: The timestamp when the file was last modified.
Last Access Time: The timestamp when the file was last accessed.
SHA256 Hash: The SHA256 hash of the file.
Integrity Check Status: A status that indicates whether the file’s hash matches the provided known hash (if given).
