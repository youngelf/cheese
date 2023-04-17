# Reads the config file, and creates holes for the config
import os


# TODO: Config starts with some other character: .
#       This makes it possible to have a config anywhere in the file.
# TODO: Read about holes, and see if it is possible to create entirely empty files.
# TODO: Commandline param on whether you want to create holes or empty files.
# TODO: Commandline param if you want to keep the hash of the files at config creation time
# TODO:

def create_skeleton(config="cheese.conf", target=".", config_make_holes=False):
    """
    Read the config provided here, and create a skeleton of cheese: files that just have names, the correct modes and
    size, but are empty (UNIX holes)
    @rtype: int
    @param target: the directory in which the skeleton is created.
    @param config: the input that is read to create a skeleton
    @return: number of empty files created
    """
    try:
        config = open(config, "r")
    except FileExistsError:
        print("Cannot open file {0}".format(config))
        return -1

    # TODO: Test that we can write to the target directory.
    # Test that the target directory has sufficient space

    # Number of files created
    num_files = 0
    # For each line in the file
    for line in config.readlines():
        if len(line) < 3:
            continue
        if line.strip()[0] == '#':
            # Ignore a comment line
            continue

        pieces = line.split(sep=',', maxsplit=3)
        if len(pieces) < 3:
            print("Ignoring: {0}".format(line))
            continue

        # Verify that the size of the file is the same as the first piece
        name_length, size, attrs, name = int(pieces[0]), int(pieces[1]), int(pieces[2]), pieces[3][1:-1]
        if not (name_length == len(name)):
            # Complain
            print("Unexpected filename: of string {0} is {1} not {1}".format(name, len(name), name_length))
            print("Will not continue on file: {0}".format(name))
            continue

        # Create the file with the right attributes
        print("Working on {0}".format(name))
        out_file = os.path.join(target, name)
        dir = os.path.dirname(out_file)
        # TODO: directories have their own attributes, we need them in the config
        os.makedirs(dir, exist_ok=True)
        f = open(out_file, "x")
        # TODO: Learn more about holes.  If the user doesn't want bookending, then let this be.
        # This works, and creates right sized files.
        if config_make_holes:
            # Create an appropriately sized hole
            f.seek(size - 1, 0)
            f.write('.')

        f.close()
        num_files = num_files + 1

    # Modify the log file pointing to what was written
    return num_files


def write_journal(journal, filename):
    """ Write the current journal to the filename provided here
    @param journal:
    @param filename:
    @rtype: object
    """
    pass


def directory_traverser(source=".", config="cheese.conf"):
    """
    Given the name of the directory, traverse it and create an config that can be shared.
    Does not overwrite the file, does not modify any files in the directory
    @rtype: int
    @param source:
    @param config:
    @return: Number of files this directory traversal produced, -1 if it failed
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
        config = open(config, "x")
    except FileExistsError:
        # Complain somehow
        print("File {0} already exists. Will not create the file.".format(config))
        return -1

    # Write toplevel config information to the file.
    config.write(config_header)
    count = 0

    # Recurse down the directory
    # For each file, get the size, and the full path
    # Add to the config.
    for dirname, subdir_list, file_list in os.walk(source, topdown=True):
        for file_name in file_list:
            print(dirname)

            full_name = os.path.join(dirname, file_name)
            info = os.stat(full_name)
            # We have to remove the toplevel directory that we are building this from, since everything is
            # relative to that directory.
            # TODO: Need to verify this crude logic works in every current system.
            prefix = len(source) + 1
            printed_name = full_name[prefix:]
            print("{0} with size {1} and mode {2}".format(printed_name, info.st_size, info.st_mode))
            # TODO: Got to figure out how best to escape and unescape strings so that they are preserved
            # TODO: Got to write some tests around this.
            config.write("{0}, {1}, {2}, {3}\n".format(len(printed_name), info.st_size, info.st_mode, printed_name))
            count = count + 1

    config.write("total_files={0}".format(count))
    return count
