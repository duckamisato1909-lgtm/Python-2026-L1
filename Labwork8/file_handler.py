import os
import pickle
import zipfile
import threading
import pandas as pd

DATA_FILE = "students.dat"

def _save_task(students, courses, marks):
    try:
        data = {
            "students": students,
            "courses": courses,
            "marks": marks
        }
        with open("temp_data.pkl", "wb") as f:
            pickle.dump(data, f)
            
        with zipfile.ZipFile(DATA_FILE, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write("temp_data.pkl", arcname="data.pkl")
            
        if os.path.exists("temp_data.pkl"):
            os.remove("temp_data.pkl")
            
        s_data = [{"id": s.get_id(), "name": s.get_name(), "dob": s.get_dob()} for s in students]
        pd.DataFrame(s_data).to_csv("students.csv", index=False)
        
        print("\n[Background Thread] Data successfully compressed and saved to students.dat")
    except Exception as e:
        print(f"\n[Background Thread] Error saving data: {e}")

def save_data(students, courses, marks):
    print("Starting background thread for data compression & storage...")
    save_thread = threading.Thread(target=_save_task, args=(students, courses, marks))
    save_thread.start()

def load_data():
    if not os.path.exists(DATA_FILE):
        return None, None, None
    
    try:
        with zipfile.ZipFile(DATA_FILE, 'r') as zipf:
            zipf.extract("data.pkl", path=".")
            
        with open("data.pkl", "rb") as f:
            data = pickle.load(f)
            
        if os.path.exists("data.pkl"):
            os.remove("data.pkl")
            
        print("Data successfully loaded and decompressed from students.dat")
        return data.get("students"), data.get("courses"), data.get("marks")
    except Exception as e:
        print(f"Error loading data: {e}")
        return None, None, None