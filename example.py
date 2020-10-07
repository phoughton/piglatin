
vowels = ['a', 'e', 'i', 'o', 'u']
inword_punctuation = ['-', "'"]
outword_punctuation = [',', '.']


def first_consonant_clust(text):
    index = 0

    while text[index: index+1].lower() not in vowels:
        if text[index: index+1].lower().isalpha():
            index += 1
        else:
            return -1

    return index


def pigify_word(in_text):
    f_cc = first_consonant_clust(in_text)

    if f_cc > 0:
        return in_text[f_cc:] + in_text[0:f_cc] + "ay"
    if f_cc == 0:
        return in_text + "yay"
    else:
        return in_text


def pigify_sentence(in_text):

    punctuation = inword_punctuation + outword_punctuation

    for char in punctuation:
        in_text = in_text.replace(char, f" {char} ")
    out = []
    for word in in_text.split():
        out.append(pigify_word(word.strip()))

    out_text = ' '.join(out)
    for char in inword_punctuation:
        out_text = out_text.replace(f" {char} ", char)

    for char in outword_punctuation:
        out_text = out_text.replace(f" {char}", char)

    return out_text


print(pigify_sentence("I found a glove-box, I explained. Said the F.B.I."))
