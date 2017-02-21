## Step 2: Write the bodies of functions get_length, is_longer, count_nucleotides, and contains_sequence

def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    
    return dna1 > dna2

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    return dna.count(nucleotide)

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    return dna2 in dna1

## Step 3: Write functions is_valid_sequence and insert_sequence

def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if a DNA sequence is valid, that is, it contains no characters other than A, T, C, and G.

    >>> is_valid_sequence("ATCGGC")
    True
    >>> is_valid_sequence("HTEYTU")
    False
    """

    validity = True

    for char in dna:
        if not char in 'ATCG':
            validity = False

    return validity

def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence at a given index.

    Precondition: DNA sequences provided are valid.

    >>> insert_sequence("CCGG", "AT", 2)
    "CCATGG"
    >>> insert_sequence("GGG", "CCC", 0)
    "CCCGGG"
    >>> insert_sequence("AAA", "TTT", -1)
    "AATTTA"
    """

    return dna1[:index] + dna2 + dna1[index:]

## Step 4: Write functions get_complement and get_complementary_sequence

def get_complement(nucleotide):
    """ (str) -> str

    Return the complement of a given nucleotide.

    Precondition: given nucleotides are valid.

    >>> get_complement("A")
    "T"
    >>> get_complement("T")
    "A"
    >>> get_complement("C")
    "G"
    >>> get_complement("G")
    "C"
    """

    if nucleotide == "A":
        return "T"
    if nucleotide == "T":
        return "A"
    if nucleotide == "C":
        return "G"
    if nucleotide == "G":
        return "C"

def get_complementary_sequence(dna):
    """ (str) -> str

    Return the complementary DNA sequence of a given DNA sequence.

    Precondition: given DNA sequences are valid.
    
    >>> get_complementary_sequence("AT")
    "TA"
    >>> get_complementary_sequence("CG")
    "GC"
    >>> get_complementary_sequence("AGTC")
    "TCAG"
    """

    comp_sequence = ""

    for nucleotide in dna:
        if nucleotide == "A":
            comp_sequence = comp_sequence + "T"
        if nucleotide == "T":
            comp_sequence = comp_sequence + "A"
        if nucleotide == "C":
            comp_sequence = comp_sequence + "G"
        if nucleotide == "G":
            comp_sequence = comp_sequence + "C"

    return comp_sequence
