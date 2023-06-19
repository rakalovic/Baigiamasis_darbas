from django.db import models


class Projektas(models.Model):
    projekto_id = models.AutoField(primary_key=True)
    projekto_pavadinimas = models.CharField(max_length=500)
    tyrimo_protokolo_numeris = models.CharField(max_length=6)
    grezinio_nr = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.projekto_pavadinimas}_{self.tyrimo_protokolo_numeris}"


class Duomenys(models.Model):
    duomenu_id = models.AutoField(primary_key=True)
    projektas = models.ForeignKey(Projektas, on_delete=models.CASCADE)
    pries_praplovima = models.DecimalField(max_digits=6, decimal_places=2)
    po_praplovimo = models.DecimalField(max_digits=6, decimal_places=2)
    sietas_8_mm = models.DecimalField(max_digits=6, decimal_places=2)
    sietas_4_mm = models.DecimalField(max_digits=6, decimal_places=2)
    sietas_2_mm = models.DecimalField(max_digits=6, decimal_places=2)
    sietas_1_mm = models.DecimalField(max_digits=6, decimal_places=2)
    sietas_0500_mm = models.DecimalField(max_digits=6, decimal_places=2)
    sietas_0250_mm = models.DecimalField(max_digits=6, decimal_places=2)
    sietas_0125_mm = models.DecimalField(max_digits=6, decimal_places=2)
    sietas_0063_mm = models.DecimalField(max_digits=6, decimal_places=2)
    sietas_0_mm = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.projektas.projekto_pavadinimas}"

