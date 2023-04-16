# Reads the config file, and creates holes for the config
import os


def read_file(config_filename):
    """ Reads the config file and carries out the specific actions."""
    # Open the file

    # For each line in the file

    # Create an appropriately sized hole

    # Modify the log file pointing to what was written
    pass


def write_journal(journal, filename):
    """ Write the current journal to the filename provided here"""
    pass


def directory_traverser(directory=".", config_filename="cheese.conf"):
    """
    Given the name of the directory, traverse it and create an config that can be shared.
    Does not overwrite the file, does not modify any files in the directory
    :param directory:
    :param config_filename:
    :return:
    """

    config_header = """# Cheese config
    version = 1
    """
    # Open file for writing
    # Fail if you cannot open the file
    try:
        config = open(config_filename, "x")
    except FileExistsError:
        # Complain somehow
        print("File {0} already exists. Will not create the file.".format(config_filename))
        return -1

    # Write toplevel config information to the file.
    config.write(config_header)
    count = 0

    # Recurse down the directory
    # For each file, get the size, and the full path
    # Add to the config.
    for filename in os.listdir(directory):
        info = os.stat(filename)
        print("{0} with size {1} and mode {2}".format(filename, info.st_size, info.st_mode))
        # TODO: Got to figure out how best to escape and unescape strings so that they are preserved
        # TODO: Got to write some tests around this.
        config.write("{0}, {1}, {2}".format(filename, info.st_size, info.st_mode))
        count = count + 1

    config.write("total_files={0}".format(count))
    return count
