
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import pandas as pd
import os

class NewCSVHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.endswith(".csv"):
            print(f"New file detected: {event.src_path}")
            new_data = pd.read_csv(event.src_path)
            
            # Load master file and append
            master_path = "supply_chain_data_master.csv"
            master_df = pd.read_csv(master_path)
            combined = pd.concat([master_df, new_data], ignore_index=True)
            combined.to_csv(master_path, index=False)

            # Optional: call analysis functions here
            run_analysis(combined)

def run_analysis(df):
    # Insert your cleaning, KPI, or model code here
    print("Running updated analysis...")

# Monitor setup
folder_to_watch = "incoming_data"
observer = Observer()
observer.schedule(NewCSVHandler(), folder_to_watch, recursive=False)
observer.start()

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    observer.stop()
observer.join()
