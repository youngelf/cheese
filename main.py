# This is a sample Python script.
import ConfigReader


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num_files = ConfigReader.directory_traverser(directory="/home/x/music", config_filename="/tmp/cheese.conf")
    print("Discovered {0} files".format(num_files))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
