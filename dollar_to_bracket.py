import re

def encase_in_square_brackets(match_obj):
    if match_obj.group() is not None:
        return r"\[" + match_obj.group()[2:-2] + r"\]"

def encase_in_round_brackets(match_obj):
    if match_obj.group() is not None:
        return r"\(" + match_obj.group()[1:-1] + r"\)"

def dollar_to_bracket_re(input_filename,output_filename="output.txt"):
    with open(input_filename,"r") as f:
        in_text = f.read()
    in_text = re.sub("[$][$].*?[$][$]",encase_in_square_brackets,in_text)
    in_text = re.sub("[$].*?[$]",encase_in_round_brackets,in_text)
    with open(output_filename,"w") as f:
        f.write(in_text)

if __name__ == "__main__":
    dollar_to_bracket_re("input.txt")