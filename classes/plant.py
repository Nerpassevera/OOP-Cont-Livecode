class Plant:

    def __init__(self, name, water_lavel, sunlight_hours, is_blooming=False):
        self.name = name
        self.water_level = water_lavel
        self.sunlight_hours = sunlight_hours
        self.is_blooming = is_blooming
        self.growth_stage = self.check_growth()

    def water(self, water_amount):
        self.water_level += water_amount
        self.check_growth()

    def give_sunlight(self, sunlight_hours_to_add):
        self.sunlight_hours += sunlight_hours_to_add
        self.check_growth()

    def check_growth(self):
        if self.water_level > 5 and self.sunlight_hours > 5:
            self.growth_stage = "Mature" 
        else:
            self.growth_stage = "Sprout"
        return self.growth_stage
    
    def __repr__(self):
        return f"A {self.name} flower with {self.water_level} water level, {self.sunlight_hours} sunlight hours which is {"not" if not self.is_blooming else None} in bloom"

plant = Plant("Orchid", 3, 2)
print(plant)
print(plant.growth_stage)