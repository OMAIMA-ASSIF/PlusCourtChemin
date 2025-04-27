 #OMAIMA ASSIF GLSID-1
def dijkstra_simple(graphe, depart):
    # Initialisation
    distances = {sommet: float('inf') for sommet in graphe}  # Initialiser toutes les distances à l'infini
    distances[depart] = 0  # Distance du point de départ à lui-même
    chemins = {sommet: [] for sommet in graphe}  # Pour stocker les chemins
    chemins[depart] = [depart]  # Chemin du départ est lui-même
    visites = set()  # les sommets déjà visités
    
    while len(visites) < len(graphe):
        # Trouver le sommet non visité le plus proche
        sommet_courant = None
        distance_min = float('inf')
        for sommet in graphe:
            if sommet not in visites and distances[sommet] < distance_min:
                sommet_courant = sommet
                distance_min = distances[sommet]
        
        if sommet_courant is None:
            break  # Tous les sommets accessibles ont été visités
            
        visites.add(sommet_courant)
        
        # Mettre à jour les distances des voisins
        for voisin, poids in graphe[sommet_courant].items():
            nouvelle_distance = distances[sommet_courant] + poids
            if nouvelle_distance < distances[voisin]:
                distances[voisin] = nouvelle_distance
                chemins[voisin] = chemins[sommet_courant] + [voisin]  # Mettre à jour le chemin
                
    return distances, chemins

# Fonction pour afficher les résultats de manière lisible
def afficher_resultats(distances, chemins):
    print("Distances minimales et chemins:")
    for sommet in sorted(distances.keys()):
        distance = distances[sommet]
        chemin = ' → '.join(chemins[sommet]) if chemins[sommet] else 'Pas de chemin'
        print(f"  {sommet}: Distance = {distance if distance != float('inf') else '∞'}, Chemin = {chemin}")

# Exemple 
graphe_test = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'D': 1},
    'C': {'A': 4, 'D': 1},
    'D': {'B': 1, 'C': 1}
}

# Test
print("\nEn utilisant l'algorithme de Dijkstra : \n")

print("Depuis A:")
distances, chemins = dijkstra_simple(graphe_test, 'A')
afficher_resultats(distances, chemins)

print("\nDepuis B:")
distances, chemins = dijkstra_simple(graphe_test, 'B')
afficher_resultats(distances, chemins)

print("\nDepuis C:")
distances, chemins = dijkstra_simple(graphe_test, 'C')
afficher_resultats(distances, chemins)

print("\nDepuis D:")
distances, chemins = dijkstra_simple(graphe_test, 'D')
afficher_resultats(distances, chemins)
