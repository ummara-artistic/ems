import os
import sys
import webbrowser
import subprocess
import time

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'labor_management.settings')

    # Open EMS in browser after a short delay
    def open_browser():
        time.sleep(2)
        webbrowser.open("http://127.0.0.1:8000")

    try:
        import threading
        threading.Thread(target=open_browser).start()

        # Run Django dev server
        from django.core.management import execute_from_command_line
        sys.argv = ["manage.py", "runserver", "127.0.0.1:8000"]
        execute_from_command_line(sys.argv)

    except Exception as e:
        print("🚨 EMS failed to start!")
        print(str(e))
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
