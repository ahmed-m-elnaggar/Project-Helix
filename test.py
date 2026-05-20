def analyze_dna(sequence):
    sequence = sequence.upper()
    
    valid_bases = set("ATCG")
    if not set(sequence).issubset(valid_bases):
        print("Error: Invalid DNA sequence. Only A, T, C, G are allowed.")
        return
    
    print("DNA Sequence:", sequence)
    print("Length:", len(sequence))
    print("A count:", sequence.count("A"))
    print("T count:", sequence.count("T"))
    print("G count:", sequence.count("G"))
    print("C count:", sequence.count("C"))
    gc_content = ((sequence.count("G") + sequence.count("C")) / len(sequence)) * 100
    print("GC content:", round(gc_content, 2), "%")

analyze_dna("HELLO")
analyze_dna("ATCGTTACGATCG")