import re

single_word_repattern = re.compile(r'\w+')
sequence_string_repattern = re.compile(r'(?:(?!,).)+(,\s*(?:(?!,).)+)*')
emptied_sequence_string_repattern = re.compile(r'(?:,|\s)*')
robota_candidate_external_id_repattern = re.compile(r'(?<=https:\/\/robota\.ua\/candidates\/)\d+')