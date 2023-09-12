# install libraries
import gzip
import sys

# create lists
Styphi_gen_list = list()
Paeruginosa_gen_list = list()

# Open ZIP files
with gzip.open('uniprotkb_proteome_Styphi.fasta.gz', 'rt') as file_1:

    # Iterates through the file lines
    for line in file_1:
        line = line.strip()  # Remove leading and trailing whitespace

        # Checks if the line is a header (starts with ">")
        if line.startswith(">"):
            # Extract the gene name
            temp = line.split()
            gene_name = temp[-3]
            gene_name = gene_name[3:]
            Styphi_gen_list.append(gene_name)

with gzip.open('uniprotkb_proteome_Paeruginosa.fasta.gz', 'rt') as file_2:

    # Iterates through the file lines
    for line in file_2:
        line = line.strip()  # Remove leading and trailing whitespace

        # Checks if the line is a header (starts with ">")
        if line.startswith(">"):
            # Extract the gene name
            temp = line.split()
            gene_name = temp[-3]
            gene_name = gene_name[3:]
            Paeruginosa_gen_list.append(gene_name)

# Convert lists into sets
Styphi_gen_set = set(Styphi_gen_list)
Paeruginosa_gen_set = set(Paeruginosa_gen_list)

# Search for identical elements
Identical_elements = Styphi_gen_set.intersection(Paeruginosa_gen_set)

# Different elements (in both lists)
Different_elements_both = Styphi_gen_set.symmetric_difference(
    Paeruginosa_gen_set)

# Diferent elements in Styphi_gen_set
Different_elements_Styphi_gen_list = Styphi_gen_set.difference(
    Paeruginosa_gen_set)

# Different elements in Paeruginosa_gen_set
Different_elements_Paeruginosa_gen_list = Paeruginosa_gen_set.difference(
    Styphi_gen_set)

# Start counter for identical elements
Counter = 0

# Iterate through the elements of one list and count the same elements in the other
for element in Styphi_gen_set:
    if element in Paeruginosa_gen_set:
        Counter += 1

# Print results

# print("Shared gens: ", Identical_elements)
# print("Different genes in both bacteria: ", Different_elements_both)
# print("Different S. typhi genes: ", Different_elements_Styphi_gen_list)
# print("Different P. aeruginosa genes: ",
#      Different_elements_Paeruginosa_gen_list)

with open('Shared Genes.txt', 'w') as archive:
    sys.stdout = archive
    print("Shared genes count: ", "\n", Counter)
    print("Shared gens: ", "\n", Identical_elements)
    print("Different genes in both bacteria: ", "\n", Different_elements_both)
    print("Different S. typhi genes: ", "\n", Different_elements_Styphi_gen_list)
    print("Different P. aeruginosa genes: ", "\n",
          Different_elements_Paeruginosa_gen_list)

sys.stdout = sys.__stdout__
