from django.db import models

class Compliment(models.Model):
    SKILLS = 'Skills'
    TRAIT = 'Trait'
    APPEARANCE = 'Appearance'
    CATEGORY_CHOICES = [
        (SKILLS, 'Skills'),
        (TRAIT, 'Trait'),
        (APPEARANCE, 'Appearance')
    ]
    category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        default=SKILLS
    )
    compliment = models.TextField()

    def __str__(self):
        return self.compliment
