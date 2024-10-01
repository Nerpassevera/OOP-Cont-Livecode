from classes.plant import Plant

def test_plant_class_creates_instance_with_attributes():
    plant_name = "Butterfly pea flower"
    plant_water_level = 6
    plant_sunlight_hours = 7
    plant_is_blooming = True

    plant = Plant(plant_name, plant_water_level, plant_sunlight_hours, plant_is_blooming)

    assert plant.name == plant_name
    assert plant.water_level == plant_water_level
    assert plant.sunlight_hours == plant_sunlight_hours
    assert plant.is_blooming == plant_is_blooming

def test_plant_class_updates_growth_stage_after_watering():
    plant_name = "Butterfly pea flower"
    plant_water_level = 3
    plant_sunlight_hours = 6
    plant_is_blooming = True
    water_to_add = 3

    plant = Plant(plant_name, plant_water_level, plant_sunlight_hours, plant_is_blooming)
    plant.water(water_to_add)


    assert plant.growth_stage == "Mature"