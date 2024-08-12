from src.inner_library import HELLO


def greetings(addition_to_greeting: str):
    print(HELLO.format(additions=addition_to_greeting))
