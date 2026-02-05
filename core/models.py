from django.db import models

class Stock(models.Model):
    symbol = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    last_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    # Financial metrics for your Analytics page
    altman_z_score = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    debt_to_equity = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    volatility = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return self.symbol