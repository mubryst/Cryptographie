# Cryptographie
TP Cryptographie Yomani (Efrei - Boris ROSE) 

TP 1 de Cryptographie
Boris Rose
2 juin 2025
1 Objectifs pédagogiques
1. Faire la distinction entre un algorithme de hachage et ses principes de robustesse et
un algorithme de chiffrement et les siens
2. Comprendre HMAC et son contexte d’utilisation applicatif
3. Déterminer les grands principes de sécurité implémenter dans le cadre d’une application
2 Serveur d’application
— Créer votre propre serveur d’application
— Utiliser les bonnes pratiques de développement notamment l’utilisation d’un fichier
.env
— Utiliser des middlewares d’authentification, de validation et de sanitizing (surtout
d’authentification)
2.1 Pour ceux qui ne veulent pas faire de serveur d’application
— Analyser le backend fait en cours et déterminer :
— Les principes de sécurité qui ont été implémentés
— proposer une analyse documentée du code en constatant les points forts et les
points faibles
— proposer des solutions pour renforcer les contrôles (middlewares) opérés par
l’application sur les données entrantes.
— Parler des principes de sécurité (du cours) que vous pouvez voir dedans
— Caractériser l’algorithme de hachage utilisé en utilisant le cours
— Justifier sa robustesse en fonction du cours
— Caractériser l’utilisation de HMAC (voir le cours) dans le cadre de la création
du Json Web Token.
— Évoquer les alternatives existantes à l’utilisation de HMAC-SHA-256

---------------------------------------------------------------------------------------------------------

TP 2 de Cryptographie

Boris Rose
3 juin 2025
1 Objectifs pédagogiques
— Comprendre la logique du chiffrements par substitution mono-alphabétique et polyalphabétique
— Déterminer les limites de ce mode de chiffrement symétrique
— Déterminer des solutions pour renforcer la confusion ( selon Shannon )
1.1 Chiffrement de César
— Définir une fonction qui lorsqu’on lui passe deux valeurs (arguments) :
— le clair
— le décalage
— retourne le chiffré qui correspond
— Faire l’inverse :
— le chiffré
— le décalage
— qui retourne le clair
2 Exercice de programmation
2.1 Chiffrement de Vigenère
— Définir une fonction qui lorsqu’on lui passe deux valeurs (arguments) :
— le clair
— la clé
— retourn le chiffré qui correspond
— Faire l’inverse :
— le chiffré
— la clé
— qui retourne le clair

-------------------------------------------------------------------------------------------------------------------
