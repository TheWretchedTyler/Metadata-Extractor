import os
import time
import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox
import csv
import json

# Global variable for storing metadata list
metadata_list = []

# Function to calculate file hash (SHA256)
def get_file_hash(file_path, hash_type="sha256"):
    hash_func = getattr(hashlib, hash_type)()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except Exception as e:
        return None

# Function to get file size in human-readable format
def get_size(file_size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if file_size < 1024.0:
            return f"{file_size:.2f} {unit}"
        file_size /= 1024.0
    return f"{file_size:.2f} TB"

# Function to check if file's hash matches a known hash (integrity check)
def check_file_integrity(file_path, known_hash):
    file_hash = get_file_hash(file_path)
    return file_hash == known_hash if file_hash else False

# Function to extract and display the metadata
def extract_metadata():
    global metadata_list  # Access the global metadata_list
    file_paths = file_path_entry.get().split(";")  # Supports multiple files
    if not file_paths:
        messagebox.showerror("Error", "No file selected.")
        return

    metadata_list = []  # Clear metadata list before appending new data
    for file_path in file_paths:
        if not os.path.exists(file_path):
            messagebox.showerror("Error", f"File {file_path} does not exist.")
            continue
        
        try:
            # Basic file information
            file_name = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)
            creation_time = time.ctime(os.path.getctime(file_path))
            modified_time = time.ctime(os.path.getmtime(file_path))
            access_time = time.ctime(os.path.getatime(file_path))
            
            # Hash and file type
            file_hash = get_file_hash(file_path, "sha256")
            file_extension = os.path.splitext(file_path)[1]

            # Integrity check with known hash
            known_hash = known_hash_entry.get()
            hash_status = check_file_integrity(file_path, known_hash) if known_hash else "N/A"

            # Append metadata for export and display
            metadata = {
                "File Name": file_name,
                "File Path": file_path,
                "File Extension": file_extension,
                "File Size": get_size(file_size),
                "Creation Time": creation_time,
                "Last Modified Time": modified_time,
                "Last Access Time": access_time,
                "SHA256 Hash": file_hash,
                "Integrity Check Status": hash_status
            }
            metadata_list.append(metadata)
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred with {file_path}: {str(e)}")
    
    # Debugging: Check the metadata list after extraction
    print("Extracted Metadata:", metadata_list)
    
    # Display and export the metadata
    display_metadata(metadata_list)

# Function to display metadata in the GUI
def display_metadata(metadata_list):
    metadata_output.config(state=tk.NORMAL)
    metadata_output.delete(1.0, tk.END)

    for metadata in metadata_list:
        for key, value in metadata.items():
            metadata_output.insert(tk.END, f"{key}: {value}\n")
        metadata_output.insert(tk.END, "-" * 60 + "\n")
    
    metadata_output.config(state=tk.DISABLED)

# Function to export metadata to CSV or JSON
def export_metadata():
    global metadata_list  # Access the global metadata_list
    if not metadata_list:
        messagebox.showerror("Error", "No metadata to export.")
        return

    export_format = export_format_var.get()

    if export_format == 'CSV':
        with open("metadata_report.csv", mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=metadata_list[0].keys())
            writer.writeheader()
            for metadata in metadata_list:
                writer.writerow(metadata)
        messagebox.showinfo("Export", "Metadata exported to metadata_report.csv")

    elif export_format == 'JSON':
        with open("metadata_report.json", mode='w') as file:
            json.dump(metadata_list, file, indent=4)
        messagebox.showinfo("Export", "Metadata exported to metadata_report.json")

# Function to browse and select files
def browse_files():
    file_paths = filedialog.askopenfilenames(title="Select Files")
    if file_paths:
        file_path_entry.delete(0, tk.END)
        file_path_entry.insert(tk.END, ";".join(file_paths))  # Support multiple file selection

# GUI setup
root = tk.Tk()
root.title("Enhanced File Metadata Extractor")
root.geometry("700x600")

# File path entry and browse button
file_path_label = tk.Label(root, text="Select files (separate multiple files with semicolon ';'):")
file_path_label.pack(pady=10)

file_path_entry = tk.Entry(root, width=50)
file_path_entry.pack(pady=5)

browse_button = tk.Button(root, text="Browse", command=browse_files)
browse_button.pack(pady=5)

# Integrity check input (known hash)
known_hash_label = tk.Label(root, text="Enter known file hash for integrity check (optional):")
known_hash_label.pack(pady=10)

known_hash_entry = tk.Entry(root, width=50)
known_hash_entry.pack(pady=5)

# Extract metadata button
extract_button = tk.Button(root, text="Extract Metadata", command=extract_metadata)
extract_button.pack(pady=20)

# Export options
export_format_var = tk.StringVar(value='CSV')
export_label = tk.Label(root, text="Export format:")
export_label.pack(pady=10)

csv_radio = tk.Radiobutton(root, text="CSV", variable=export_format_var, value='CSV')
csv_radio.pack(pady=5)

json_radio = tk.Radiobutton(root, text="JSON", variable=export_format_var, value='JSON')
json_radio.pack(pady=5)

# Export metadata button
export_button = tk.Button(root, text="Export Metadata", command=export_metadata)
export_button.pack(pady=20)

# Text box to display metadata
metadata_output = tk.Text(root, height=15, width=70, wrap=tk.WORD, state=tk.DISABLED)
metadata_output.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
