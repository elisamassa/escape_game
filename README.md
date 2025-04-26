import json
import os

FICHIER_SAUVEGARDE = "sauvegarde.json"

def reinitialiser_jeu():
    return {"decryptage": False, "empreintes": False, "course": False, "interrogatoire": False}

def charger_jeu():
    if os.path.exists(FICHIER_SAUVEGARDE):
        with open(FICHIER_SAUVEGARDE, "r") as fichier:
            return json.load(fichier)
    return reinitialiser_jeu()

def sauvegarder_jeu(etat):
    with open(FICHIER_SAUVEGARDE, "w") as fichier:
        json.dump(etat, fichier)

def afficher_menu():
    print("🔍 MENU PRINCIPAL")
    print("1. Nouvelle enquête")
    print("2. Continuer enquête en cours")
    choix = input("Choix (1 ou 2) : ")
    return reinitialiser_jeu() if choix == "1" else charger_jeu()

def mini_jeu_decryptage():
    print("\n🔐 Décryptage du message mystérieux")
    for tentative in range(3):
        reponse = input("Code à déchiffrer : AL IRENO → ").upper()
        if reponse == "LEONARD":
            print("✅ Bonne réponse !")
            return True
        if tentative == 1:
            print("💡 Indice : nom du meurtrier griffonné par la victime...")
        print("❌ Mauvais code.")
    return False

def mini_jeu_empreintes():
    print("\n🧬 Analyse des empreintes digitales")
    empreintes_scene = ["ABC123", "XYZ789", "LMN456"]
    suspects = {"Marie": "ABC123", "Lucas": "XYZ789", "Joséphine": "LMN456"}
    print("Empreintes détectées :", ", ".join(empreintes_scene))
    print("Analyse des suspects :")
    for nom, code in suspects.items():
        if code in empreintes_scene:
            print(f"👉 Empreinte retrouvée : {nom}")
    return True

def mini_jeu_course():
    print("\n🏃 Course poursuite du suspect")
    bonnes_reponses = ["gauche", "raccourci", "sauter"]
    score = 0
    questions = [
        "Le suspect tourne à gauche ou à droite ?",
        "Faut-il continuer tout droit ou prendre un raccourci ?",
        "Faut-il sauter ou éviter l'obstacle ?"
    ]
    for i, question in enumerate(questions):
        reponse = input(question + " > ").lower()
        if reponse == bonnes_reponses[i]:
            print("✅ Bonne décision !")
            score += 1
        else:
            print("❌ Mauvais choix.")
    return score >= 2

def mini_jeu_interrogatoire():
    print("\n🗨️ Interrogatoire final du suspect")
    print("Choisissez la bonne preuve pour piéger le suspect :")
    print("1. Ticket de caisse")
    print("2. Photo trop ancienne")
    print("3. Billet d’avion prouvant que sa femme n’était pas chez lui")
    choix = input("Votre choix (1, 2 ou 3) : ")
    return choix == "3"

def jeu_principal():
    etat = afficher_menu()
    input("\nAppuyez sur Entrée pour commencer votre enquête...")

    if not etat["decryptage"]:
        etat["decryptage"] = mini_jeu_decryptage(); sauvegarder_jeu(etat)
    if not etat["empreintes"]:
        etat["empreintes"] = mini_jeu_empreintes(); sauvegarder_jeu(etat)
    if not etat["course"]:
        etat["course"] = mini_jeu_course(); sauvegarder_jeu(etat)
    if not etat["interrogatoire"]:
        etat["interrogatoire"] = mini_jeu_interrogatoire(); sauvegarder_jeu(etat)

    print("\n🎉 Enquête terminée ! Le coupable était Léonard, ancien bras droit du maire.")
    print("Merci pour votre travail, détective.")

if __name__ == "__main__":
    jeu_principal()
