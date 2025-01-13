import logging
import os
from datetime import datetime

# Create a log file with a timestamped name
Log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # %S replaced with %M for minutes
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)  # Create the logs directory if it doesn't exist

# Final log file path
log_file_path = os.path.join(logs_path, Log_file)

# Set up logging configuration
logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,  # Use logging.INFO instead of logging.info
)

# Test the logger
if __name__ == "__main__":
    logging.info("Logging has started")

