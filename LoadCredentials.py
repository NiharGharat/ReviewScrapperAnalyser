import configparser


def loadCredentials(path_to_config_file):
    config_file = configparser.ConfigParser()
    config_file.read(path_to_config_file)
    mongo_config = config_file["MONGO"]

    dict_of_credentials = {}
    for key in mongo_config:
        print("Key was " + key + " and value was " + mongo_config[key])
        dict_of_credentials[key] = mongo_config[key]
    return dict_of_credentials


if __name__ == '__main__':
    loadCredentials("credentials.config")
