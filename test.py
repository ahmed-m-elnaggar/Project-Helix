def analyze_dna(sequence):
    sequence = sequence.upper()
    
    valid_bases = set("ATCG")
    if not set(sequence).issubset(valid_bases):
        print("Error: Invalid DNA sequence. Only A, T, C, G are allowed.")
        return
    
    print("--- DNA ANALYSIS ---")
    print("Sequence:", sequence)
    print("Length:", len(sequence))
    print("A count:", sequence.count("A"))
    print("T count:", sequence.count("T"))
    print("G count:", sequence.count("G"))
    print("C count:", sequence.count("C"))
    gc_content = ((sequence.count("G") + sequence.count("C")) / len(sequence)) * 100
    print("GC content:", round(gc_content, 2), "%")

def compare_sequences(seq1, seq2):
    seq1 = seq1.upper()
    seq2 = seq2.upper()
    
    if len(seq1) != len(seq2):
        print("Error: Sequences must be the same length to compare.")
        return
    
    mutations = []
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            mutations.append((i, seq1[i], seq2[i]))
    
    print("--- MUTATION DETECTION ---")
    print("Sequence 1:", seq1)
    print("Sequence 2:", seq2)
    print("Mutations found:", len(mutations))
    for m in mutations:
        print(f"Position {m[0]}: {m[1]} → {m[2]}")

analyze_dna("ATCGTTACGATCG")
print()
compare_sequences("ATCGTTACGATCG", "ATCGTAACGTTCG")