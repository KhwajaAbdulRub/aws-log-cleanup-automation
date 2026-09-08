import os
import time
import logging
import argparse

# Configure logging to output to both a file and the terminal
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    handlers=[
        logging.FileHandler('cleanup_audit.log'),
        logging.StreamHandler()
    ]
)

def cleanup_stale_logs(target_dir, retention_days):
    """Scans a directory and permanently deletes files older than retention_days."""
    if not os.path.exists(target_dir):
        logging.error(f"Target directory '{target_dir}' does not exist.")
        return 0

    # Convert days to seconds (86,400 seconds in a day)
    retention_seconds = retention_days * 86400
    current_time = time.time()
    deleted_count = 0

    logging.info(f"Initiating cleanup in '{target_dir}' for files older than {retention_days} days.")

    for filename in os.listdir(target_dir):
        filepath = os.path.join(target_dir, filename)
        
        # Verify it is a file and not a nested directory
        if os.path.isfile(filepath):
            file_age = current_time - os.path.getmtime(filepath)
            
            if file_age > retention_seconds:
                try:
                    os.remove(filepath)
                    logging.info(f"PURGED: {filepath}")
                    deleted_count += 1
                except PermissionError:
                    logging.error(f"PERMISSION DENIED: Could not delete {filepath}. Check Linux user privileges.")
                except Exception as e:
                    logging.error(f"ERROR: Failed to delete {filepath}. Reason: {e}")

    logging.info(f"Cleanup complete. Total files purged: {deleted_count}")
    return deleted_count

if __name__ == '__main__':
    # argparse allows a DevOps engineer to pass arguments directly from the Linux terminal
    parser = argparse.ArgumentParser(description="Automated DevSecOps Log Rotation Utility")
    parser.add_argument('-d', '--directory', type=str, required=True, help="Target directory to clean")
    parser.add_argument('-r', '--retention', type=int, default=30, help="Number of days to keep files (default: 30)")
    
    args = parser.parse_args()
    cleanup_stale_logs(args.directory, args.retention)