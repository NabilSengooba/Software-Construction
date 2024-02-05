import shutil

def check_disk_usage(disk, min_absolute, min_percent):
    """
    Checks if there is enough free disk space.

    Args:
        - disk (str): The disk path to check.
        - min_absolute (int): The minimum absolute free space required in bytes.
        - min_percent (int): The minimum percentage of free space required.

    Returns:
        - bool: True if there is enough free space, False otherwise.
    """
    # Get disk usage statistics
    du = shutil.disk_usage(disk)

    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total

    # Calculate the amount of free space in gigabytes
    gigabytes_free = du.free / 2**30

    # Check if free space is below the specified thresholds
    if percent_free < min_percent or gigabytes_free < min_absolute:
        # If not enough free space, return False
        return False

    # If there is enough free space, return True
    return True

# Check for at least 2 GB and 10% free space on the root ("/") disk
if not check_disk_usage("/", 2*2**30, 10):
    # Print an error message if there is not enough disk space
    print("ERROR: Not enough disk space")
    # Return error code 1 if there is not enough disk space
    return 1

# Print a success message if there is enough disk space
print("Everything ok")
# Return success code 0
return 0
