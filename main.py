# This is a sample Python script.
import ConfigReader


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def create_config():
    # Use a breakpoint in the code line below to debug your script.
    num_files = ConfigReader.directory_traverser(source="/home/x/music", config="/tmp/cheese.conf")
    print("Discovered {0} files".format(num_files))


def create_skel():
    # Use a breakpoint in the code line below to debug your script.
    num_files = ConfigReader.create_skeleton(config="/tmp/cheese.conf", target="/tmp/x-empty")
    print("Discovered {0} files".format(num_files))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # create_config()
    create_skel()
