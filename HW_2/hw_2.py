### CODE FOLLOWS FROM THIS POINT FORWARD ###

import collections
import operator


alphabet = "abcdefghijklmnopqrstuvwxyz"

freq_dict = { "A": .08167, "B": .01492, "C": .02782, "D": .04253, "E": .12702, "F": .02228,
"G": .02015, "H": .06094, "I": .06996, "J": .00153, "K": .00772, "L": .04025,
"M": .02406, "N": .06749, "O": .07507, "P": .01929, "Q": .00095, "R": .05987,
"S": .06327, "T": .09056, "U": .02758, "V": .00978, "W": .02360, "X": .00150,
"Y": .01974, "Z": .00074 }


plaintext = """ethicslawanduniversitypolicieswarningtodefendasystemyouneedtobeabletothinklikeanattackerandthatincludesunderstandingtechniquesthatcanbeusedtocompromisesecurityhoweverusingthosetechniquesintherealworldmayviolatethelawortheuniversitysrulesanditmaybeunethicalundersomecircumstancesevenprobingforweaknessesmayresultinseverepenaltiesuptoandincludingexpulsioncivilfinesandjailtimeourpolicyineecsisthatyoumustrespecttheprivacyandpropertyrightsofothersatalltimesorelseyouwillfailthecourseactinglawfullyandethicallyisyourresponsibilitycarefullyreadthecomputerfraudandabuseactcfaaafederalstatutethatbroadlycriminalizescomputerintrusionthisisoneofseverallawsthatgovernhackingunderstandwhatthelawprohibitsifindoubtwecanreferyoutoanattorneypleasereviewitsspoliciesonresponsibleuseoftechnologyresourcesandcaenspolicydocumentsforguidelinesconcerningproper"""


def english_variance():
    count = 0
    sum = 0
    for letter in freq_dict:
        count += 1
        sum += freq_dict[letter]
    mean = sum /count
    diff = 0
    for letter in freq_dict:
        diff += pow(freq_dict[letter] - mean, 2)
    print "English Text Variance: " + str(diff / count)

def text_variance(input, name):
    text_count = collections.Counter(input)
    for letter in text_count:
        text_count[letter] = float(text_count[letter]/(1.0 * len(input)))

    count = 0
    sum = 0
    diff = 0

    for letter in text_count:
        count += 1
        sum += text_count[letter]


    mean = sum / count

    for letter in text_count:
        diff += pow(text_count[letter] - mean, 2)



    print name + " Text Variance: " + str(diff / count)

def  vigenere_variance(input, key_length, name):
    texts = [""] * key_length
    for x in range(key_length):
        texts[x] = input[x::key_length]

    texts_counts = [0.0] * key_length
    for x in range(key_length):
        texts_counts[x] = collections.Counter(texts[x])


    for x in range(key_length):
        count = 0
        for letter in texts_counts[x]:
            count += texts_counts[x][letter]
        for letter in texts_counts[x]:
            texts_counts[x][letter] = float(texts_counts[x][letter] / (1.0 * count))


    overall_sum = 0
    for x in range(key_length):


        count = 0
        sum = 0
        diff = 0

        for letter in texts_counts[x]:
            count += 1
            sum += texts_counts[x][letter]

        mean = sum / count

        for letter in texts_counts[x]:
            diff += pow(texts_counts[x][letter] - mean, 2)
        overall_sum += (diff / count)
    print name + " Vigenere Variance Mean: " + str(overall_sum / key_length)
    return overall_sum / key_length

def vigenere_cipher(message, key):
    output = ""
    key_ind = 0
    for letter in message:
        letter_num = alphabet.find(letter) + alphabet.find(key[key_ind])
        letter_num %= len(alphabet)
        output += alphabet[letter_num]


        key_ind += 1
        if key_ind >= len(key):
            key_ind = 0
    return output

def vigenere_frequency_attack(message, key_length):

    possible_key = ""
    # get individual letter frequencies for given key length
    texts = [""] * key_length
    for x in range(key_length):
        texts[x] = message[x::key_length]

    texts_counts = [0.0] * key_length
    for x in range(key_length):
        texts_counts[x] = collections.Counter(texts[x])

    for x in range(key_length):
        count = 0
        for letter in texts_counts[x]:
            count += texts_counts[x][letter]
        for letter in texts_counts[x]:
            texts_counts[x][letter] = float(texts_counts[x][letter] / (1.0 * count))
    # assume that the most common letter maps to e for each letter in key and add the guess onto possible key
    for x in range(key_length):
        sorted_freqs = sorted(texts_counts[x].items(), key=operator.itemgetter(1), reverse=True)
        guess = sorted_freqs[0][0]
        print sorted_freqs
        possible_key += alphabet[(alphabet.find(guess.lower()) - alphabet.find("e")) % len(alphabet)]
    print possible_key
    return possible_key





def vigenere_decrypt(message, key):
    output = ""
    key_ind = 0
    for letter in message:
        letter_num = alphabet.find(letter) - alphabet.find(key[key_ind])
        letter_num %= len(alphabet)
        output += alphabet[letter_num]

        key_ind += 1
        if key_ind >= len(key):
            key_ind = 0
    return output


def main():
    # print vigenere_decrypt(vigenere_cipher(plaintext, "goodtry"), "goodtry") == plaintext
    print "Part 1.A"
    english_variance()
    print
    print

    print "Part 1.B"
    text_variance(plaintext, "Plaintext")
    print
    print

    print "Part 1.C"
    VC1 = vigenere_cipher(plaintext, "yz")
    text_variance(VC1, "VCipher 'yz'")


    VC2 = vigenere_cipher(plaintext, "xyz")
    text_variance(VC2, "VCipher 'xyz'")

    VC3 = vigenere_cipher(plaintext, "wxyz")
    text_variance(VC3, "VCipher 'wxyz'")

    VC4 = vigenere_cipher(plaintext, "vwxyz")
    text_variance(VC4, "VCipher 'vwxyz'")

    VC5 = vigenere_cipher(plaintext, "uvwxyz")
    text_variance(VC5, "VCipher 'uvwxyz'")
    print
    print

    print "Part 1.D"
    vigenere_variance(VC1, 2, "VCipher 'yz'")
    vigenere_variance(VC2, 3, "VCipher 'xyz'")
    vigenere_variance(VC3, 4, "VCipher 'wxyz'")
    vigenere_variance(VC4, 5, "VCipher 'vwxyz'")
    vigenere_variance(VC5, 6, "VCipher 'uvwxyz'")
    print
    print

    print "Part 1.E"
    for x in range(1, 7):
        vigenere_variance(VC5, x, "Variance for key of size " + str(x) + ":")
    print
    print

    print "Part 2"
    ciphertext = """MOOYRFCSAICGEPYLTYIFMEOTZIKARFJPHWCISSHSKPPOCFRMZSXMEVTETESJKXCEMSCTXNTIMYCKXAIHSOGVYLIGSKJMRQSHAPYTSCSMSEIODHIPOMZPMHFDBLASVETLPPWGGOIJPRBYAKMEVBYGPHCOGRELFXMLEEOWZILMEZOFGXEHBMUILEDFRYHAZLAKTHADUZVYCGDEKGPAKOUOGWSRHAPHSSWTRBQECKZFXTTFFNAIZPRZCUKBTBZDWEWNVFLDBRCWEWSESHOLLBFUMSXQYJOYKBEHEOCREJAKMYSVVAIHSCNRHESOWWSASSLJXCYIOCUXXUPHLQAPMOGOIKDLBMHOLEHFBLBWMLLBOSTYDEOOBXLRIMEKBNEQVPILFAIOXCNYTLTYSVVWEWNVVLMBWYJXCYRGPTNWAPGSSLAEKHDCFFCECQVXCTFAPQKLNFBRCOPRDOCRXYFBBNSLDPVWYUHYTESYSBRHYCCGMSEAICGEPYPVLRTDMXZWGHYCXZWSWOUAZPMTYDFBEVXTRLDTBBZNQVPFXHAPBZTBYEOPZMTYYTVPFXEHBRFFLWEVGSOWPVBFJHATNDHSSRHAKHPRUFTQVPMTWSLVLRTDEZFPHTYDQVPWKRRBOESLEFBOCKTDTEOEGHXEYCOMPZUIROWLNOSSCWMEHBMOWWYTQVTBDEHBMNCNWDYSLFBEICOYMHYECCFBWZUQOMCNETESACMEEOGXFLAOQHPFPLSJFDRNCSISJGLTSQSCPNETESJVTONQAPHYZRPSGSKLLVSLFLTNCONHFCSAICGEPYMFPHXYDBRDVXOIABEVTGEXGTGMPRYSNONDEESCGBDTBFLBWSEOUZCWQOOBZHATNDVFGULNAKPFXLSRBOIKDLBMTGALSFHHOLAOPGTPEPTLPPHAPDRFDZXJSPVFRWPRBRECMSIKYHVTETESYSBRHYCCGPZUIRDORTFQVPDHETBFDOKCISSOWGEHBGEFXPTQVPRNCSISJGDYETHSOMEHBDZHMPRPVLRTDMXZWGHYTLCMIMEHBMSOWYESSCSOPNPSPBATMQVTGUZYTODOGZTESCUHZDOSLGHYFLFVSXAIKUEVXAOQHPFLLWXMEVXJDFRYHPLNQRFREPYJWIWGRWFHSOVSIIRWWDPTEOEKAPNJFLBWXRPRFFLWEVKZYXFPLBEVXOUIZRFTJTRSDRTJORFDHHCYPHLFMDTESCSPLSKCEVBYGXPZIMEHBQWCNOYPYJCNESFRPHHD"""
    possible_values = []
    # iterate through key lengths and see which ones have a proper variance for english text
    for x in range(1, 27):
       if vigenere_variance(ciphertext, x, "Variance for key of size " + str(x) + ":") >= 0.0008:
           possible_values.append(x)
    print
    print "Possible Key Lengths:" + str(possible_values)
    print
    # most likely key value is 7 since it is the GCD of the possible values
    print vigenere_decrypt(ciphertext.lower(), vigenere_frequency_attack(ciphertext, 7))
    # frequency attack worked except for a single letter, the last one has a 'c' when it should be an 'r'
    print alphabet[(alphabet.find("c") - alphabet.find("r")) % len(alphabet)]
    # last letter should be an l
    print vigenere_decrypt(ciphertext.lower(), "axolotl")
    # decrypted to the correct plaintext

if __name__ == "__main__":
    main()
