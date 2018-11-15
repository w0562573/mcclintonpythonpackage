import dendropy
import os.path

def sequence_reader(filepath):
       # check that the file exists by 
    assert os.path.exists(filepath)
    sequence_set = dendropy.DnaCharacterMatrix.get(
        path=filepath,
        schema="phylip"
)

#check the returned type - should be dendropy character matrix
    assert type(sequence_set) == dendropy.datamodel.charmatrixmodel.DnaCharacterMatrix
    return(sequence_set)
