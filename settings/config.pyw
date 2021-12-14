import toml

class settings():
    config = toml.load("H:\RPS Machiene\settings\config.toml")
    rounds = config["Game"]["rounds"]
