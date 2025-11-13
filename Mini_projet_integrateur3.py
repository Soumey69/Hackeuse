# 🎯 Exercice : Saisie et affichage des utilisateurs (avec classe)
# -------------------------------------------------
#Le programme demande à l'utilisateur son prénom et son âge,
# détermine s'il est majeur ou mineur, stocke les infos dans un dictionnaire,
# puis affiche la liste complète à la fin.
# -------------------------------------------------
# Partie 1 : on recueille les informations sous forme de dictionnaires
# Partie 2 : on crée des objets Utilisateur à partir de ces dictionnaires
# -------------------------------------------------

# Liste pour stocker les utilisateurs sous forme de dictionnaires
utilisateurs = []

print("=== 👋 Bienvenue dans le programme Utilisateurs ===\n")

# Demander combien de personnes l'utilisateur veut saisir
nb = int(input("Combien d'utilisateurs veux-tu ajouter ? "))

# Boucle de saisie
for i in range(nb):
    print(f"\n--- Utilisateur {i + 1} ---")
    nom = input("➡️  Entrez votre prénom : ").capitalize()
    age = int(input("➡️  Entrez votre âge : "))

    utilisateur = {"nom": nom, "age": age}

    # Vérifier la majorité
    if age >= 18:
        print(f"✅ {nom} est majeur·e.")
    else:
        print(f"🚸 {nom} est mineur·e.")

    utilisateurs.append(utilisateur)

# Afficher la liste complète
print("\n=== 📋 Liste complète des utilisateurs ===")
for u in utilisateurs:
    print(f"- {u['nom']} ({u['age']} ans)")

# -------------------------------------------------
# Partie 2 : Classe Utilisateur
# -------------------------------------------------
class Utilisateur:
    """Classe représentant un utilisateur avec nom et âge."""
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def dire_bonjour(self):
        """Affiche un message personnalisé."""
        statut = "majeur·e ✅" if self.age >= 18 else "mineur·e 🚸"
        print(f"Bonjour, je m'appelle {self.nom}, j'ai {self.age} ans et je suis {statut}.")

# Transformer les dictionnaires en objets de la classe Utilisateur
liste_objets = [Utilisateur(u["nom"], u["age"]) for u in utilisateurs]

# Fonction pour faire dire bonjour à tous les utilisateurs
def saluer_tous(liste):
    print("\n=== 👋 Salutations des utilisateurs ===\n")
    for user in liste:
        user.dire_bonjour()

# Appel de la fonction
saluer_tous(liste_objets)

print("\nProgramme terminé 👋 Merci d’avoir participé !")
