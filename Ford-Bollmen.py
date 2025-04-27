 #OMAIMA ASSIF GLSID-1

from collections import defaultdict

def creer_graphe():
    
    return {
        'graphe': defaultdict(dict),
        'sommets': set()
    }

def ajouter_arc(g, u, v, poids):
    """Ajoute un arc orienté avec son poids"""
    g['sommets'].update([u, v])
    g['graphe'][u][v] = poids

def verifier_circuit_absorbant(g):
    """Vérifie la présence de circuits absorbants (somme des poids < 0)"""
    dist = {s: 0 for s in g['sommets']}
    
    for _ in range(len(g['sommets']) - 1):
        for u in g['graphe']:
            for v, p in g['graphe'][u].items():
                if dist[v] > dist[u] + p:
                    dist[v] = dist[u] + p
    
    # Vérification des circuits absorbants
    for u in g['graphe']:
        for v, p in g['graphe'][u].items():
            if dist[u] + p < dist[v]:
                return True
    return False

def calculer_predecesseurs(g):
    """Calcule les prédécesseurs pour chaque sommet"""
    pred = defaultdict(set)
    for u in g['graphe']:
        for v in g['graphe'][u]:
            pred[v].add(u)
    return pred

def ordonnancement_niveaux(g):
    """Retourne les sommets ordonnancés par niveaux"""
    if verifier_circuit_absorbant(g):
        raise ValueError("Erreur: Le graphe contient un cycle absorbant. Impossible de continuer.")
    
    niveaux = []
    pred = calculer_predecesseurs(g)
    restants = set(g['sommets'])
    
    while restants:
        courant = {s for s in restants if not pred[s] & restants}
        if not courant:
            raise ValueError("Erreur: Le graphe contient un cycle (non absorbant). Impossible d'ordonnancer.")
        niveaux.append(courant)
        restants -= courant
    return niveaux

def calculer_m_et_chemins(g, source):
    """Calcule les distances minimales m(x) depuis la source et les chemins correspondants"""
    if verifier_circuit_absorbant(g):
        raise ValueError("Erreur: Le graphe contient un cycle absorbant. Algorithme non applicable.")
    
    try:
        niveaux = ordonnancement_niveaux(g)
    except ValueError as e:
        raise
        
    m = {s: float('inf') for s in g['sommets']}
    m[source] = 0
    chemins = {s: [] for s in g['sommets']}
    chemins[source] = [source]
    
    for niveau in niveaux:
        for u in niveau:
            for v, p in g['graphe'][u].items():
                if m[u] + p < m[v]:
                    m[v] = m[u] + p
                    chemins[v] = chemins[u] + [v]
    return m, chemins

# Exemple d'utilisation
def main():
    # Graphe normal
    g = creer_graphe()
    ajouter_arc(g, "x0", "x1", 2)
    ajouter_arc(g, "x0", "x2", 4)
    ajouter_arc(g, "x1", "x3", -1)
    ajouter_arc(g, "x1", "x4", 1)
    ajouter_arc(g, "x2", "x3", 3)
    ajouter_arc(g, "x3", "x5", 2)
    ajouter_arc(g, "x4", "x5", 3)

    # Graphe avec cycle absorbant
    ga = creer_graphe()
    ajouter_arc(ga, "A", "B", -1)
    ajouter_arc(ga, "B", "C", -2)
    ajouter_arc(ga, "C", "A", -3)

    try:
        print("=== Étapes de l'algorithme ===")
        
        # Vérification circuit absorbant
        if verifier_circuit_absorbant(g):
            raise ValueError("Erreur: Le graphe contient un cycle absorbant. Impossible de continuer.")
        print("1. Vérification circuit absorbant: ✅ Absent")
        
        # Ordonnancement par niveaux
        print("2. Ordonnancement par niveaux:")
        niveaux = ordonnancement_niveaux(g)
        for i, niveau in enumerate(niveaux):
            print(f"   Niveau {i}: {niveau}")
        
        # Calcul des m(x) et des chemins
        print("3. Calcul des m(x) depuis x0 avec chemins:")
        m, chemins = calculer_m_et_chemins(g, "x0")
        for sommet in sorted(m.keys()):
            print(f"   m({sommet}) = {m[sommet] if m[sommet] != float('inf') else '∞'} \t Chemin: {' → '.join(chemins[sommet]) if chemins[sommet] else '-'}")
        
        
            
    except ValueError as e:
        print(e)
        exit(1)

    # Test avec le graphe contenant un cycle absorbant
    try:
        print("\nTest avec graphe contenant cycle absorbant:")
        if verifier_circuit_absorbant(ga):
            print("Erreur détectée: Le graphe contient un cycle absorbant.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
