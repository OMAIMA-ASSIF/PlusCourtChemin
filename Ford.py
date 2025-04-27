 #OMAIMA ASSIF GLSID-1

from collections import defaultdict

def creer_graphe():
    """Initialise une structure de graphe"""
    return {
        'graphe': defaultdict(dict),
        'sommets': set()
    }

def ajouter_arc(g, u, v, poids):
    """Ajoute un arc orienté avec son poids"""
    g['sommets'].update([u, v])
    g['graphe'][u][v] = poids

def bellman_ford_simple(g, source):
    """Implémentation simplifiée de Bellman-Ford sans affichage des étapes"""
    # Initialisation
    distances = {s: float('inf') for s in g['sommets']}
    distances[source] = 0
    chemins = {s: [] for s in g['sommets']}
    chemins[source] = [source]
    
    # Relaxation des arcs
    for _ in range(len(g['sommets']) - 1):
        mise_a_jour = False
        for u in g['graphe']:
            for v, poids in g['graphe'][u].items():
                if distances[u] + poids < distances[v]:
                    distances[v] = distances[u] + poids
                    chemins[v] = chemins[u] + [v]
                    mise_a_jour = True
        
        if not mise_a_jour:
            break
    
    # Vérification des circuits absorbants
    for u in g['graphe']:
        for v, poids in g['graphe'][u].items():
            if distances[u] + poids < distances[v]:
                return distances, chemins, True
    
    return distances, chemins, False

def afficher_resultats(distances, chemins):
    """Affiche les résultats finaux de manière claire"""
    print("\nRésultats finaux: x0 comme origine")
    print("Sommet".ljust(8), "Distance".ljust(10), "Chemin")
    for sommet in sorted(distances.keys()):
        dist = distances[sommet] if distances[sommet] != float('inf') else "∞"
        chemin = '→'.join(chemins[sommet]) if chemins[sommet] and distances[sommet] != float('inf') else "-"
        print(f"{sommet}".ljust(8), f"{dist}".ljust(10), f"{chemin}")

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

    print("=== Algorithme de Bellman-Ford simplifié ===")
    
    distances, chemins, circuit_absorbant = bellman_ford_simple(g, "x0")
    
    if circuit_absorbant:
        print("\n⚠️ Attention: le graphe contient un circuit absorbant (poids négatif)")
    else:
        afficher_resultats(distances, chemins)

if __name__ == "__main__":
    main()
