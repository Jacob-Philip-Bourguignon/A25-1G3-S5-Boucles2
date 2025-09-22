import pytest
from SolutionDebug2 import retrait

#Arrange
def test_retrait():
    solde = 1000
    montant = 400
    resultat_attendu = 600

    resultat_obtenu =  retrait(solde, montant)

    assert resultat_attendu == resultat_obtenu
