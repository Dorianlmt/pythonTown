# Codes de couleurs ANSI
RESET = "\033[0m"
YELLOW = "\033[93m"  # Actions
VIOLET = "\033[95m"  # Leia
RED = "\033[91m"     # Dark Vador
GREEN = "\033[92m"   # Luke
BLUE = "\033[94m"    # Wuher

# Classe de base : Personnage
class Personnage:
    def __init__(self, nom, boisson_favorite="eau"):
        self.__nom = nom
        self.__boisson_favorite = boisson_favorite
        self.__color = RESET  # Couleur par défaut

    def set_color(self, color):
        self.__color = color

    def parle(self, texte):
        print(f"{self.__color}{self.__nom} - {RESET}{texte}")

    def se_presenter(self):
        self.parle(f"Bonjour, je suis {self.quel_est_ton_nom()} et j’aime le {self.__boisson_favorite}.")

    def boire(self):
        print(f"{YELLOW}Ah ! Un bon verre de {self.__boisson_favorite} ! GLOUPS !{RESET}")

    def quel_est_ton_nom(self):
        return self.__nom

    def quel_est_ta_boisson_favorite(self):
        return self.__boisson_favorite


# Classe Jedi
class Jedi(Personnage):
    def __init__(self, nom, boisson_favorite="thé vert galactique", sabre_couleur="bleu"):
        super().__init__(nom, boisson_favorite)
        self.__sabre_couleur = sabre_couleur
        self.__popularite = 0
        self.set_color(GREEN)

    def combattre(self, sith):
        print(f"{YELLOW}Le Jedi {self.quel_est_ton_nom()} brandit son sabre {self.__sabre_couleur} et attaque {sith.quel_est_ton_nom()}. ZWOOM !{RESET}")
        self.parle("Que la Force soit avec moi !")

    def sauver(self, prisonnier):
        if not prisonnier.est_libre():
            prisonnier.se_faire_liberer()
            self.__popularite += 1
        else:
            self.parle(f"{prisonnier.quel_est_ton_nom()} est déjà libre !")

    def se_presenter(self):
        super().se_presenter()
        self.parle(f"Mon sabre-laser est de couleur {self.__sabre_couleur}.")
        self.parle(f"Ma popularité dans la galaxie est de {self.__popularite}.")


# Classe Sith
class Sith(Personnage):
    def __init__(self, nom, boisson_favorite="chocolat chaud", apparence="sombre", prime=5000):
        super().__init__(nom, boisson_favorite)
        self.__apparence = apparence
        self.__prisonniers = 0
        self.__prime = prime
        self.set_color(RED)

    def capturer(self, cible):
        if cible.est_libre():
            cible.se_faire_kidnapper()
            self.__prisonniers += 1
            self.parle(f"Ah ah ! {cible.quel_est_ton_nom()}, tu es désormais mon prisonnier !")
        else:
            self.parle(f"{cible.quel_est_ton_nom()} est déjà capturé !")

    def se_presenter(self):
        super().se_presenter()
        self.parle(f"Je suis connu pour mon apparence {self.__apparence}.")
        self.parle(f"J’ai capturé {self.__prisonniers} âmes dans la galaxie.")
        self.parle(f"Ma tête est mise à prix {self.__prime} crédits !")


# Classe Rebelle
class Rebelle(Personnage):
    def __init__(self, nom, boisson_favorite="lait bleu", mission="libérer la galaxie"):
        super().__init__(nom, boisson_favorite)
        self.__mission = mission
        self.__libre = True
        self.set_color(VIOLET)

    def changer_de_mission(self, nouvelle_mission):
        self.__mission = nouvelle_mission
        self.parle(f"Ma nouvelle mission est {nouvelle_mission} !")

    def se_faire_kidnapper(self):
        self.__libre = False
        self.parle("Non ! Je suis capturé par l'Empire !")

    def se_faire_liberer(self):
        self.__libre = True
        self.parle("Merci pour votre aide, ami(e) !")

    def est_libre(self):
        return self.__libre

    def se_presenter(self):
        super().se_presenter()
        self.parle(f"Ma mission actuelle est {self.__mission}.")


# Classe Cantinier
class Cantinier(Personnage):
    def __init__(self, nom, boisson_favorite="vin des étoiles", cantina=None):
        super().__init__(nom, boisson_favorite)
        self.__cantina = cantina if cantina else f"Cantina de {nom}"
        self.set_color(BLUE)

    def parle(self, texte):
        super().parle(f"{texte} mon ami.")

    def se_presenter(self):
        super().se_presenter()
        self.parle(f"Je tiens la célèbre {self.__cantina}.")

    def servir(self, personnage):
        self.parle(f"Voici un verre de {personnage.quel_est_ta_boisson_favorite()} pour {personnage.quel_est_ton_nom()} !")
        personnage.boire()


# Test des classes
if __name__ == "__main__":
    # Création des personnages
    rebelle = Rebelle("Leia", mission="renverser l'Empire")
    sith = Sith("Vador", apparence="terrifiant")
    jedi = Jedi("Luke", sabre_couleur="vert")
    cantinier = Cantinier("Wuher")

    # Présentations
    rebelle.se_presenter()
    sith.se_presenter()
    jedi.se_presenter()
    cantinier.se_presenter()

    # Actions
    print(f"{YELLOW}\nLa Cantina sert des boissons :{RESET}")
    cantinier.servir(rebelle)
    cantinier.servir(sith)
    cantinier.servir(jedi)

    print(f"{YELLOW}\nHistoire :{RESET}")
    sith.capturer(rebelle)
    jedi.combattre(sith)
    jedi.sauver(rebelle)
    rebelle.changer_de_mission("reconstruire l'Alliance Rebelle")

    # Réaffichage des présentations
    print(f"{YELLOW}\nAprès les événements...{RESET}")
    rebelle.se_presenter()
    sith.se_presenter()
    jedi.se_presenter()
