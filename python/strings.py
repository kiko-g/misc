def trimUselessWhitespaces(text: str):
    return " ".join(text.split())


if __name__ == "__main__":
    text = """wlqkfejf
    f   wflqwkfgw

    rrrrrrrrr              3333333
    b rqtbeq     qerq     veqrre
    """

    clean_text = trimUselessWhitespaces(text)
    print(clean_text)
