import sys
from lingaai.interpreter import executer

def main():
    if len(sys.argv) != 2:
        print("Utilisation : lingaai mon_fichier.lga")
        return
    with open(sys.argv[1], 'r') as fichier:
        code = fichier.read()
        executer(code)
