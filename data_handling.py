import os
import yaml
import json

def read_yaml(file_path):
    with open(file_path) as yaml_file:
        file_data = yaml.load(yaml_file, Loader=yaml.CLoader)
    return file_data


def to_yaml(dict_file, file_path):
    with open(file_path, 'w+') as f_out:
        f_out.write(yaml.dump(dict_file))
    return


def read_json(file_path):
    with open(file_path) as json_file:
        file_data = json.load(json_file)
    return file_data


def to_json(dict_file, file_path):
    with open(file_path, 'w+') as f_out:
        f_out.write(json.dumps(dict_file))
    return


def read_atlas(file_path):
    from atlas_data import read_atlas
    df = read_atlas.AtlasData(file_path)
    return df


def get_list_of_directories(file_path):
    list_dirs = []
    for el in os.listdir(file_path):
        if os.path.isdir(el):
            list_dirs.append(el)
    return list_dirs


def get_list_of_filenames(file_path='.', ext='txt'):
    list_files = []
    for file in os.listdir(file_path):
        if file.endswith(ext):
            list_files.append(file)
    return list_files