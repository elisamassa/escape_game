import pygame

# ------------------------
# 🔐 Mini-jeu 1 : Décryptage
# ------------------------

def jeu_decryptage():
    code = "AL IRENO"           # Le message codé trouvé sur la scène de crime
    solution = "LEONARD"        # Ce que le joueur doit deviner
    tentatives = 0              # Compteur de tentatives
    indice_donne = False        # Est-ce que l’indice a déjà été affiché ?
    saisie = ""                 # Ce que le joueur est en train d’écrire

    while True:
        pygame.event.pump()    # Actualise l'état des événements clavier/souris
        ecran = pygame.display.get_surface()
        ecran.fill((30, 30, 30))  # Nettoie l'écran (fond noir)

        # Affichage du texte à l'écran
        afficher_texte("Décryptez le mot trouvé sur la scène :", 50, 50)
        afficher_texte(f"Message : {code}", 50, 100)
        afficher_texte(f"Réponse : {saisie}", 50, 150)

        if tentatives == 2 and not indice_donne:
            afficher_texte("💡 Indice : C'est un prénom, écrit dans le sang...", 50, 200, (180,180,180))
            indice_donne = True

        afficher_texte("Appuie sur Entrée pour valider", 50, 250, (180,180,180))
        pygame.display.flip()

        # Lecture des événements clavier
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    tentatives += 1
                    if saisie.upper() == solution:
                        return True  # Réussite
                    else:
                        saisie = ""  # Efface la réponse pour recommencer

                elif event.key == pygame.K_BACKSPACE:
                    saisie = saisie[:-1]  # Supprime le dernier caractère
                else:
                    saisie += event.unicode  # Ajoute le caractère tapé

        pygame.time.wait(30)  # Petite pause pour fluidifier la boucle

# ------------------------
# 🧬 Mini-jeu 2 : Empreintes digitales
# ------------------------

def jeu_empreintes():
    ecran = pygame.display.get_surface()

    # Empreintes retrouvées sur la scène
    empreintes_scene = ["ABC123", "XYZ789", "LMN456"]

    # Dictionnaire des suspects avec leurs empreintes
    suspects = {
        "Marie": "ABC123",
        "Dorian": "QWE852",
        "Lucas": "XYZ789",
        "Joséphine": "LMN456",
        "Lucie": "RTY963"
    }

    ecran.fill((30, 30, 30))  # Fond noir
    afficher_texte("Empreintes digitales retrouvées :", 50, 50)
    y = 100  # Position verticale

    # Boucle sur les suspects pour trouver ceux dont l'empreinte est sur la scène
    for nom, code in suspects.items():
        if code in empreintes_scene:
            afficher_texte(f"Empreinte retrouvée : {nom}", 50, y)
            y += 40

    afficher_texte("Clique pour continuer", 50, y + 40, (180, 180, 180))
    pygame.display.flip()
    attendre_clic()
    return True  # Réussite automatique (jeu d'observation)

# ------------------------
# 🏃 Mini-jeu 3 : Course poursuite
# ------------------------

def jeu_course():
    ecran = pygame.display.get_surface()

    # Liste d’étapes avec une question et la bonne réponse
    etapes = [
        {"question": "Le suspect tourne à gauche ou à droite ?", "bonne": "gauche"},
        {"question": "Tout droit ou raccourci ?", "bonne": "raccourci"},
        {"question": "Sauter ou éviter l'obstacle ?", "bonne": "sauter"}
    ]

    score = 0  # Score = nombre de bonnes décisions

    for etape in etapes:
        saisie = ""  # Réponse du joueur à cette étape
        bonne = etape["bonne"]  # La bonne réponse attendue

        while True:
            ecran.fill((30, 30, 30))
            afficher_texte("Course poursuite", 50, 40, (20, 90, 200))
            afficher_texte(etape["question"], 50, 100)
            afficher_texte(f"Réponse : {saisie}", 50, 160)
            afficher_texte("Appuie sur Entrée pour valider", 50, 220, (180, 180, 180))
            pygame.display.flip()

            # Gestion du clavier
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if saisie.lower() == bonne:
                            score += 1
                        saisie = ""
                        break
                    elif event.key == pygame.K_BACKSPACE:
                        saisie = saisie[:-1]
                    else:
                        saisie += event.unicode
            else:
                continue
            break

    return score >= 2  # Le joueur doit réussir au moins 2 étapes sur 3

# ------------------------
# 🗨️ Mini-jeu 4 : Interrogatoire
# ------------------------

def jeu_interrogatoire():
    ecran = pygame.display.get_surface()
    ecran.fill((30, 30, 30))

    afficher_texte("Interrogatoire du suspect Lucas", 50, 40, (20, 90, 200))

    # Dialogue affiché à l’écran
    lignes = [
        "Q1 : Qui peut confirmer que vous étiez chez vous ?",
        "R : Ma femme était présente.",
        "Q2 : Pourquoi votre ADN est sur la scène ?",
        "R : J’ai vu le maire à 14h ce jour-là.",
        "Q3 : Pourquoi avez-vous une arme similaire ?",
        "R : Quelqu’un l’a laissée devant chez moi ce matin."
    ]

    y = 100
    for ligne in lignes:
        afficher_texte(ligne, 50, y)
        y += 30

    # Choix de preuve à l’écran
    afficher_texte("Choisis la bonne preuve pour le piéger :", 50, y + 30)
    afficher_texte("1. Ticket de caisse", 50, y + 70)
    afficher_texte("2. Photo ancienne", 50, y + 110)
    afficher_texte("3. Billet d’avion (sa femme était absente)", 50, y + 150)
    pygame.display.flip()

    # Attente du choix joueur
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    return True   # Bonne preuve
                elif event.key in [pygame.K_1, pygame.K_2]:
                    return False  # Mauvaise preuve

# ------------------------
# FONCTIONS COMMUNES POUR AFFICHER / ATTENDRE
# ------------------------

# Affichage d’un texte sur l’écran Pygame
def afficher_texte(texte, x, y, couleur=(255, 255, 255), taille=28):
    police = pygame.font.SysFont("arial", taille)
    rendu = police.render(texte, True, couleur)
    ecran = pygame.display.get_surface()
    ecran.blit(rendu, (x, y))

# Attente d’un clic souris
def attendre_clic():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return