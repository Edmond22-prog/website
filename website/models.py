from django.db import models


class Profil(models.Model):
    nom = models.CharField(max_length=255, blank=True, null=True)
    prenom = models.CharField(max_length=255, blank=True, null=True)
    localisation = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField()
    photo_profil = models.ImageField(blank=True, null=True, upload_to="images/profile/")
    photo_arriere_plan = models.ImageField(blank=True, null=True, upload_to="images/background/")
    lien_twitter = models.CharField(max_length=255, blank=True, null=True)
    lien_instagram = models.CharField(max_length=255, blank=True, null=True)
    lien_linkedin = models.CharField(max_length=255, blank=True, null=True)
    lien_github = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    numero_telephone = models.CharField(max_length=255, blank=True, null=True)
    niveau_etude = models.CharField(max_length=255, blank=True, null=True)
    date_anniversaire = models.DateField(auto_now_add=False, auto_now=False, blank=True)

    def __str__(self):
        return self.prenom+" "+self.nom


class Skill(models.Model):
    nom = models.CharField(max_length=255, blank=True, null=False)
    capacite = models.IntegerField(null=False, blank=True)
    categorie = models.CharField(max_length=255, choices=[("Technologie", "Technologie"), ("Langage", "Langage")],
                                null=False, default="Langage")

    def __str__(self):
        return self.nom + " | " + str(self.capacite) + " %"


class Diplome(models.Model):
    intitule = models.CharField(max_length=255, blank=True, null=True)
    debut_annee = models.IntegerField(null=False, blank=True)
    fin_annee = models.IntegerField(null=False, blank=True)
    nom_etablisement = models.CharField(max_length=255, blank=True, null=True)
    pays = models.CharField(max_length=255, blank=True, null=True)
    ville = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.intitule


class Experience(models.Model):
    titre = models.CharField(max_length=255, blank=True, null=True)
    periode_commencement = models.CharField(max_length=255, blank=True, null=True)
    periode_fin = models.CharField(max_length=255, blank=True, null=True)
    nom_compagnie = models.CharField(max_length=255, blank=True, null=True)
    pays = models.CharField(max_length=255, blank=True, null=True)
    ville = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.titre


class Communautaire(models.Model):
    role = models.CharField(max_length=255, blank=True, null=True)
    period_commencement = models.CharField(max_length=255, blank=True, null=True)
    periode_fin = models.CharField(max_length=255, blank=True, null=True)
    nom_compagnie = models.CharField(max_length=255, blank=True, null=True)
    pays = models.CharField(max_length=255, blank=True, null=True)
    ville = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.role


class Item_portfolio(models.Model):
    categorie = models.CharField(max_length=255, choices=[("Application", "Application"), ("Web", "Web")], null=False, default="Application")
    client = models.CharField(max_length=255, blank=True, null=True)
    lien_projet = models.CharField(max_length=255, blank=True, null=True)
    image_projet_1 = models.ImageField(blank=True, null=False, upload_to="images/portfolio/")
    image_projet_2 = models.ImageField(blank=True, null=True, upload_to="images/portfolio/")
    image_projet_3 = models.ImageField(blank=True, null=True, upload_to="images/portfolio/")
    detail = models.TextField()

    def __str__(self):
        return self.lien_projet + " || " + self.categorie