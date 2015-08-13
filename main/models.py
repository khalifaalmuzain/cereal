from django.db import models

# Create your models here.

class Manufacturer(models.Model):
	name = models.CharField(max_length=40, unique=True)

	def __unicode__(self):
		return self.name

class Cereal(models.Model):
	name = models.CharField(max_length=30, unique=True)
	type = models.CharField(max_length=2, null=True)
	manufacturer = models.ForeignKey('main.Manufacturer', null=True)
	image = models.ImageField(upload_to="cereal", null=True)
	info = models.TextField()


	def __unicode__(self):
		return self.name

class Nutrition(models.Model):
	calories = models.IntegerField(null=True)
	protein = models.IntegerField(null=True)
	fat = models.IntegerField(null=True)
	sodium = models.FloatField(null=True)
	dietary_fiber = models.FloatField(null=True)
	carbs = models.FloatField(null=True)
	sugars = models.FloatField(null=True)
	display_Shelf = models.IntegerField(null=True)
	potassium = models.IntegerField(null=True)
	vitamins_and_minerals = models.IntegerField(null=True)
	serving_size_weight = models.FloatField(null=True)
	cups_per_serving = models.FloatField(null=True)
	cereal = models.OneToOneField('main.Cereal')

	def __unicode__(self):
		return self.cereal.name

	def nutrition_value(self):
		value_list=[]
		value_list.append("Calories: %s" % self.calories)
		value_list.append("Protein: %s" % self.protein)
		value_list.append("Fat: %s" % self.fat)
		value_list.append("Sodium: %s" % self.sodium)
		value_list.append("Dietary Fiber: %s" % self.dietary_fiber)
		value_list.append("Carbs: %s" % self.carbs)
		value_list.append("Sugar: %s" % self.sugars)
		value_list.append("Display Shelf: %s" % self.display_Shelf)
		value_list.append("Potassium: %s" % self.potassium)
		value_list.append("Vitamins and Minerals: %s" % self.vitamins_and_minerals)
		value_list.append("Serving Size Weight: %s" % self.serving_size_weight)
		value_list.append("Cups Per Serving: %s" % self.cups_per_serving)


		return value_list


	


		