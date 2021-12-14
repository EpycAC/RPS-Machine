import toml

class settings():
    config = toml.load("config.toml")
    rounds = config["Game"]["rounds"]
