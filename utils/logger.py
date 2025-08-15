import datetime
import os
from colorama import Fore

LOG_DIR = 'output'

class Logger:
    def __init__(self, token_identifier="MAIN"):
        self.token_id = token_identifier
        self.log_file_path = os.path.join(LOG_DIR, f"log_{self.token_id}_{datetime.date.today()}.txt")
        os.makedirs(LOG_DIR, exist_ok=True)

    def _log(self, level, color, message):
        timestamp = datetime.datetime.now().strftime('%H:%M:%S')
        console_msg = f"{color}[{timestamp}] [{self.token_id}] [{level.upper()}] {message}{Fore.RESET}"
        file_msg = f"[{datetime.datetime.now().isoformat()}] [{self.token_id}] [{level.upper()}] {message}\n"
        
        print(console_msg)
        with open(self.log_file_path, 'a', encoding='utf-8') as f:
            f.write(file_msg)

    def info(self, message):
        self._log('info', Fore.CYAN, message)

    def success(self, message):
        self._log('success', Fore.GREEN, message)

    def warning(self, message):
        self._log('warning', Fore.YELLOW, message)

    def error(self, message):
        self._log('error', Fore.RED, message)