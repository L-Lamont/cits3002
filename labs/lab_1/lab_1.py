def hamming_distance(codeword_1, codeword_2):
#   Assumes codewords are binary and codewords are same length
#   Checks strings are same length
#   Loops over strings counting differences
#   Fails if it encounters a non binary digit

    counter = 0

    for i in range(len(codeword_1)):

        if codeword_1[i] != codeword_2[i]:
                counter += 1

    return counter

def checking_codewords(codewords, received_data):
#   Assumes codewords are binary and codewords and received data are same length
#   Check lowest hamming distance between code words
#       > lowest hamming - 1 == num errors that can be detected
#       > (lowest hamming - 1 ) / 2 = num errors that can be corrected
#   Calculate lowest hamming distance between a codeword and received_data = LHD
#   If LHD <= 2 * hamming distance between code words + 1 correct the error
#   else return error detected

    HD = hamming_distance(codewords[0], codewords[1])

    for i in codewords:
        for j in codewords:
            if i == j:
                continue

            hammingDist = hamming_distance(i, j)

            if hammingDist < HD:
                HD = hammingDist

    closestCodeword = codewords[0]
    CHD = hamming_distance(codewords[0], received_data)

    for codeword in codewords:
        hammingDist = hamming_distance(codeword, received_data)

        if hammingDist < CHD:
            CHD = hammingDist
            closestCodeword = codeword

    if CHD * 2 + 1 <= HD:
        return closestCodeword

    return "error detected"


codewords = ['0000000000', '1111100000', '1111111111']
received_data = '0000000011'

corrected = checking_codewords(codewords, received_data)
print(corrected)
