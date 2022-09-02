from django.db import models


class consultations(models.Model):
    consultation_id = models.SmallAutoField(db_column='Consultation_ID', primary_key=True, editable=False)


    class Meta:
        db_table = 'Consultations'
        verbose_name_plural = "Consultations"

    def __str__(self):
        return self.consultation_id


        