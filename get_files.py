import os


def get_files(dir_path, file_extension=None):
    if not os.path.exists(dir_path):
        print(f"{dir_path} does not exist.")
        return []
    elif not os.path.isdir(dir_path):
        print(f"{dir_path} is not a directory.")
        return []

    file_list = []

    item_list = os.listdir(dir_path)
    for item in item_list:
        item_path = os.path.join(dir_path, item)
        if os.path.isfile(item_path):
            if file_extension is None or item_path.endswith(file_extension):
                file_list.append(item_path)
        elif os.path.isdir(item_path):
            file_list.extend(get_files(item_path, file_extension))

    return file_list
