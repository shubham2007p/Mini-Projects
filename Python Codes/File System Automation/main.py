import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pymupdf

class event_handler(FileSystemEventHandler):
    
    def on_created(self, event):
        if event.is_directory:
            return
        if not event.src_path.lower().endswith('.pdf'):
            return
            
        print(f"Created {event.src_path}")
        
        # Wait until the file is fully copied/written and unlocked by the writing process.
        max_retries = 20
        retry_delay = 0.5
        doc = None
        
        for i in range(max_retries):
            try:
                # Try opening the file to verify it is no longer locked
                with open(event.src_path, 'rb'):
                    pass
                doc = pymupdf.open(event.src_path)
                break
            except (PermissionError, FileNotFoundError, pymupdf.mupdf.FzErrorSystem, pymupdf.FileDataError):
                time.sleep(retry_delay)
                
        if doc is None:
            print(f"Error: Could not open {event.src_path} (file might still be locked or missing).")
            return
            
        try:
            if len(doc) > 0:
                text = doc[0].get_text()
                print(text)
            else:
                print("PDF is empty")
            
            try:
                for page in doc:
                    for annot in page.annots():
                        rect = annot.rect
                        annotated_text = page.get_text("text", clip=rect)
                        if annotated_text.strip():
                            print(f"highlighted text: {annotated_text.strip()}")
            except Exception as e:
                print(f"Error reading PDF content: {e}")
        finally:
            doc.close()
    
    def on_modified(self, event):
        print(f"modified {event.src_path}")


observer = Observer()
event_handler = event_handler()

observer.schedule(event_handler,r'C:\Users\shubh\Downloads\idea projects\systems\books to notes\books', recursive=False)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
    print("Observer stopped")
observer.join()