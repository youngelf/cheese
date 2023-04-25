import argparse, os, sys

import ConfigReader

# The top-level code for invoking both the skeleton creation, or config creation.
# TODO: Got to write a man page, a real one.

verbose = False

def create_config(source_dir, config_name):
    # Create a config to mirror the given a source directory
    num_files = ConfigReader.create_config(source=source_dir, config=config_name)
    print("Discovered {0} files".format(num_files))


def create_skel(target_dir, config_name):
    # Given the config file, create a skeleton that mirrors the original source that created the config
    num_files = ConfigReader.create_skeleton(config=config_name, target=target_dir)
    print("Created {0} files".format(num_files))


# TODO: allow reading argparse.
def main():
    usage = """ Utility to create skeletons and configs
 This utility will create a configuration that can be taken to another location in
the filesystem and turned into a skeleton filesystem.
 
Examples:
    # Create a config file from the source directory
    {0} config -s <path/to/source> -c <config-name>
    
    # Use a previous config to create a skeleton
    {0} skeleton -c <config-name> -d </path/to/destination>

    """.format(os.path.basename(sys.argv[0]))
    parser = argparse.ArgumentParser(usage=usage, description="Act upon skeleton filesystems")
    binary_choices = ['true', 't', 'false', 'f']
    parser.add_argument('command', choices=['config', 'skeleton'],
                        help="Command, creates either a config or creates a skeleton directory")
    # TODO: move to pathlib.Path here, rather than ascii
    parser.add_argument('-s', '--source', type=ascii, default=".",
                        help="If provided, the directory to read for creating config. Otherwise, current directory")

    parser.add_argument('-d', '--destination', type=ascii, default=".",
                        help="If provided, the directory to write skeleton to. Otherwise, current directory")

    parser.add_argument('-c', '--config', type=ascii, default="/tmp/cheese.conf",
                        help="If provided, the name of config file to read or write. Otherwise, /tmp/cheese.conf")

    # Not utilized currently, let's keep it for the future.
    parser.add_argument('-n', '--dry-run', choices=binary_choices,
                        help="If true, do not modify files")

    args = parser.parse_args()

    if verbose:
        print("#", args)

    # Super ugly hackery: argparse quotes the ascii input, so we get '/tmp/cheese.conf' when we really want just
    # the path.  Right now, just removing the leading and training quotes.  This is just plain ugly.
    command = args.command.lower()
    if command == 'config':
        create_config(config_name=args.config[1:-1], source_dir=args.source[1:-1])
    elif command == 'skeleton':
        create_skel(target_dir=args.destination[1:-1], config_name=args.config[1:-1])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # create_config()
    # create_skel()
    main()
