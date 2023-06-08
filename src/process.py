import re

"""
def read_txt_files(directory):
    all_text = ""
    for root, dirs, files in os.walk(directory):
        for file in files:
            for i in range(0, 10):  # TODO - à modifier
                if file.endswith(".txt"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r") as txt_file:
                        content = txt_file.read()
                        # Do something with the content of the text file

    all_text += content
    return all_text

text = read_txt_files("../../rapbot/data")# open(path_to_file, 'r').read() # loading text dataset
"""


if __name__ == '__main__':

    # Reading input texts
    print("----- Processing rap texts with Sagemaker.")
    path_input_data = '../data/raplyrics.txt'  # where to find the data locally  # TODO - à modifier
    text = open(path_input_data, 'r').read()[:100000]  # loading text dataset # TODO - à corriger

    # clean texts
    text = text.replace('\x10', ' ')
    text = text.replace('\x14', ' ')
    text = text.replace('\x01', ' ')
    text = text.replace('\x1c', ' ')
    text = text.replace('\x13', ' ')
    text = text.replace('\x12', ' ')
    text = text.replace('\x7f', ' ')
    text = text.replace('\x0f', ' ')
    text = text.replace('\x02', ' ')
    text = text.replace('\x0e', ' ')
    text = re.sub(r'[^\x00-\x7f]', r'', text)  # removing non ascii characters

    # Output results
    path_output_data = ""  # TODO - à modifier
    with open(path_output_data, 'w') as f:
        f.write(text)
