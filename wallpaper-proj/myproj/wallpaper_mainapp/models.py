from django.db import models


class Image(models.Model):
    name = models.CharField(
        max_length=255, 
        verbose_name = "Название"
        )
    
    url = models.TextField(
        verbose_name="Ссылка"
    )
    
    category = models.ForeignKey(
        "Category",
        on_delete=models.PROTECT,
        verbose_name="Категория",
        
        )
    
    published = models.DateTimeField(
        auto_now_add=True, 
        db_index=True,
        verbose_name="Дата публикации"
        )

    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    

class Category(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="Название"
        )
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    