# ESCAPE GAME - ENQUÊTE POLICIÈRE
# Script principal du jeu
# Avec musiques, images, dialogues animés et mini-jeux

import pygame  # Bibliothèque pour créer le jeu
import sys  # Pour quitter le jeu
import json  # Pour sauvegarder/charger la partie
from escape_mini_jeux import jeu_decryptage, jeu_empreintes, jeu_course, jeu_interrogatoire

# === CONFIGURATION ===
LARGEUR, HAUTEUR = 1280, 720  # Taille de la fenêtre
FPS = 60
TAILLE_TEXTE = 30
FICHIER_SAUVEGARDE = "savegame.json"

# === COULEURS ===
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
GRIS = (180, 180, 180)
BLEU = (20, 90, 200)
ROUGE = (200, 30, 30)
FOND = (30, 30, 30)

# === INITIALISATION PYGAME ===
pygame.init()
pygame.mixer.init()  # Initialiser l’audio
pygame.mixer.music.load("ambiance.mp3")  # Musique d’ambiance
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)  # En boucle

# Fenêtre de jeu
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("🔍 Enquête Policière")
horloge = pygame.time.Clock()

# Police
police = pygame.font.SysFont("georgia", TAILLE_TEXTE)


# === FONCTION POUR JOUER LE SON DE MACHINE À ÉCRIRE ===
def jouer_machine():
    son = pygame.mixer.Sound("machineecrire.wav")
    son.set_volume(0.2)
    son.play()


# === AFFICHAGE D’UNE IMAGE EN FOND ===
def dessiner_fond(nom_image):
    image = pygame.image.load(nom_image + ".png")  # Charger l'image PNG
    image = pygame.transform.scale(image, (LARGEUR, HAUTEUR))  # Redimensionner
    flou = pygame.Surface((LARGEUR, HAUTEUR))
    flou.set_alpha(60)  # Légère opacité pour l’effet de flou
    flou.fill(NOIR)
    fenetre.blit(image, (0, 0))
    fenetre.blit(flou, (0, 0))


# === AFFICHER UN TEXTE LETTRE PAR LETTRE AVEC EFFET MACHINE ===
def afficher_texte_animé(lignes, couleur=BLANC):
    y = 100
    for ligne in lignes:
        texte = ''
        for caractere in ligne:
            texte += caractere
            dessiner_fond(fond_actuel)
            surface = police.render(texte, True, couleur)
            fenetre.blit(surface, (100, y))
            pygame.display.flip()
            jouer_machine()
            pygame.time.wait(40)
        y += 60
    attendre_clic()


# === MESSAGE TEMPORAIRE CENTRAL ===
def afficher_message_temporaire(texte, couleur=BLANC):
    dessiner_fond(fond_actuel)
    texte_surface = police.render(texte, True, couleur)
    rect = texte_surface.get_rect(center=(LARGEUR // 2, HAUTEUR // 2))
    fenetre.blit(texte_surface, rect)
    pygame.display.flip()
    pygame.time.wait(2000)


# === ATTENDRE UN CLIC ===
def attendre_clic():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.time.Clock().tick(FPS)


# === SAUVEGARDE ===
def sauvegarder(etat):
    with open(FICHIER_SAUVEGARDE, 'w') as fichier:
        json.dump(etat, fichier)


def charger():
    try:
        with open(FICHIER_SAUVEGARDE, 'r') as fichier:
            return json.load(fichier)
    except:
        return {
            "decryptage": False,
            "empreintes": False,
            "course": False,
            "interrogatoire": False,
            "fin": False
        }


# === MENU DE DÉMARRAGE ===
def afficher_menu():
    while True:
        fenetre.fill(FOND)
        titre = police.render("🔍 Enquête Policière - Escape Game", True, BLEU)
        nouvelle = police.render("1. Nouvelle Partie", True, BLANC)
        charger = police.render("2. Charger la Partie", True, GRIS)
        fenetre.blit(titre, (100, 100))
        fenetre.blit(nouvelle, (100, 200))
        fenetre.blit(charger, (100, 260))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return {
                        "decryptage": False,
                        "empreintes": False,
                        "course": False,
                        "interrogatoire": False,
                        "fin": False
                    }
                elif event.key == pygame.K_2:
                    return charger()


# === BOUCLE PRINCIPALE DU JEU ===
def jeu():
    global fond_actuel
    etat = afficher_menu()

    # INTRODUCTION
    if not etat["decryptage"]:
        fond_actuel = "intro"
        dessiner_fond(fond_actuel)
        afficher_texte_animé([
            "🕵️‍♂️ Inspecteur, un meurtre a été commis...",
            "Le maire de Montferrand a été retrouvé sans vie dans son bureau.",
            "Vous avez 4 épreuves à résoudre pour trouver le coupable."
        ])

    # JEU 1 : DECRYPTAGE
    if not etat["decryptage"]:
        fond_actuel = "decryptage"
        afficher_texte_animé([
            "🧩 Étape 1 : Décryptage",
            "Un message codé a été trouvé sur la scène de crime..."
        ])
        if jeu_decryptage():
            afficher_message_temporaire("✅ Message déchiffré : ALIRENO")
            etat["decryptage"] = True
            sauvegarder(etat)
        else:
            afficher_message_temporaire("❌ Erreur de décryptage...")

    # JEU 2 : EMPREINTES
    if not etat["empreintes"]:
        fond_actuel = "empreintes"
        afficher_texte_animé([
            "🔬 Étape 2 : Empreintes",
            "Une empreinte a été trouvée sur l’arme du crime."
        ])
        if jeu_empreintes():
            afficher_message_temporaire("✅ Correspondance trouvée.")
            etat["empreintes"] = True
            sauvegarder(etat)
        else:
            afficher_message_temporaire("❌ Ce n’est pas la bonne empreinte...", ROUGE)

    # JEU 3 : POURSUITE
    if not etat["course"]:
        fond_actuel = "poursuite"
        afficher_texte_animé([
            "🏃 Étape 3 : Poursuite",
            "Un suspect s’échappe... Attrape-le !"
        ])
        if jeu_course():
            afficher_message_temporaire("✅ Le suspect est arrêté !")
            etat["course"] = True
            sauvegarder(etat)
        else:
            afficher_message_temporaire("❌ Il a filé entre les mailles...", ROUGE)

    # JEU 4 : INTERROGATOIRE
    if not etat["interrogatoire"]:
        fond_actuel = "interrogatoire"
        afficher_texte_animé([
            "🗣️ Étape 4 : Interrogatoire",
            "Il est temps de faire avouer le suspect..."
        ])
        if jeu_interrogatoire():
            afficher_message_temporaire("✅ Il a craqué... L’aveu est clair.")
            etat["interrogatoire"] = True
            sauvegarder(etat)
        else:
            afficher_message_temporaire("❌ Il garde le silence... Il faudra plus de preuves.", ROUGE)

    # FIN
    if not etat["fin"]:
        fond_actuel = "fin"
        afficher_texte_animé([
            "✅ Enquête Résolue !",
            "Le coupable était Léonard, l’ancien bras droit du maire.",
            "Bravo inspecteur, vous avez mené l’affaire à terme."
        ])
        etat["fin"] = True
        sauvegarder(etat)
        attendre_clic()


# === DÉMARRAGE ===
if __name__ == "__main__":
    jeu()
