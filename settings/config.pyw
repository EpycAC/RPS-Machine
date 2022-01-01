import toml

class settings():
    path = __file__.replace("config.pyw", "")
    config = toml.load(path + "config.toml")
    rounds = config["Game"]["rounds"]
    profile = config["Game"]["profile"]
