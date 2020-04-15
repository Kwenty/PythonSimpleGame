class Prompt:
    @staticmethod
    def prompt(text, prompt_type, values=[]):
        while True:
            try:
                prompt = prompt_type(input(text))
                if len(values) != 0 and prompt not in values:
                    raise ImpossibleValue
                break
            except ValueError:
                print("Wrong type, " + prompt_type.__name__ + " expected")
            except ImpossibleValue:
                print("Impossible value")
        return prompt


class ImpossibleValue(Exception):
    pass
