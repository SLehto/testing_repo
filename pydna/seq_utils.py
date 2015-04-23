def complement_codon(input_codon):
    if is_codon_correct(input_codon) is True:
        print('hurraa')
    else:
        print('my bad')
        return None
        
    base_complements = {
            'A': 'T',
            'T': 'A',
            'C': 'G',
            'G': 'C',
            '?': '?',
    }

    first_base = input_codon[0]
    second_base = input_codon[1]
    third_base = input_codon[2]
        
    first_complemented_base = base_complements[first_base]
    second_complemented_base = base_complements[second_base]
    third_complemented_base = base_complements[third_base]

    complemented_codon = first_complemented_base + second_complemented_base + third_complemented_base
    
    return complemented_codon
    
    print(complemented_codon)

def is_codon_correct(input_codon):
    if type(input_codon) == float:
        return False
        
    allowed_characters = ['A', 'T', 'C', 'G', 'N', '?', '-']
    
    for base in input_codon:
        if base.upper() in allowed_characters:
            continue
        else:
            print('your codon is bad')
            return False
    return True

codon = 'AAA'
complement_codon(codon)
