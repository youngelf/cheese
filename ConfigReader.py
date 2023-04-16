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
# Comments start with # character, empty lines are fine.
version = 1
author = cheese.python
production = False

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
    for dirname, subdir_list, file_list in os.walk(directory, topdown=True):
        for file_name in file_list:
            print(dirname)

            full_name = os.path.join(dirname, file_name)
            info = os.stat(full_name)
            # We have to remove the toplevel directory that we are building this from, since everything is
            # relative to that directory.
            # TODO: Need to verify this crude logic works in every current system.
            prefix = len(directory) + 1
            printed_name = full_name[prefix:]
            print("{0} with size {1} and mode {2}".format(printed_name, info.st_size, info.st_mode))
            # TODO: Got to figure out how best to escape and unescape strings so that they are preserved
            # TODO: Got to write some tests around this.
            config.write("{0}, {1}, {2}, {3}\n".format(len(printed_name), info.st_size, info.st_mode, printed_name))
            count = count + 1

    config.write("total_files={0}".format(count))
    return count
