from Bio.PDB import *
from Bio import SeqIO

pdb_path = '7cwp.pdb'  ##change this for each file

atom_seq={}
with open(pdb_path, 'r') as pdb_file:
    for chain in SeqIO.parse(pdb_file, 'pdb-atom'):
        atom_seq[chain.id] = str(chain.seq)
no_chains = len(atom_seq)

seqres={}
with open(pdb_path, 'r') as pdb_file:
    for chain in SeqIO.parse(pdb_file, 'pdb-seqres'):
        seqres[chain.id] = str(chain.seq)

start=0
end=0
sub_seq1=''
sub_seq2=''
seqres_match={}

for chain in atom_seq:
    sub_seq1 = atom_seq[chain].split('X')[0]
    sub_seq2 = atom_seq[chain].split('X')[-1]
    start = seqres[chain].index(sub_seq1)
    end = seqres[chain].index(sub_seq2) + len(sub_seq2)
    seqres_match[chain] = seqres[chain][start:end]

atom_seq_full = seqres_match
id_seq = next(iter(atom_seq_full))
sequence = next(iter(atom_seq_full.items()))[1]

ofile = open("seq.fasta", "w")
ofile.write(">" + id_seq + "\n" +sequence + "\n")
ofile.close()

# print('Primary sequence: ', seqres)
# print('Atoms sequence (3D): ', atom_seq_full)
