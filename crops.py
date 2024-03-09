class crop():
    #parameters
    #name: use common name so no fancy biological terms
    #crop_yield: stores a percentage of the proportion that this crop grows under normal conditions.
    #status: "Ready to harvest", "Plant crop", "Vulnerable to environment"
    #water_need: The amount of water (in mm) that this crop needs on a INSERT daily/monthly/weekly
    #temp_need: The amount of "hotness" this crop needs. Measured in Farenheit (the best unit of temperature)
    
    #figure out how to integrate this....
    #pest_resist: string that contains the pestistides that are used on a crop
    
    #size: Measure of how big this crop is in sq miles
    #Note: individual crops of the same type should be clustered together for simplicity of this project 
    def __init__(self, name, crop_yield, status, water_need, temp_need, pest_resist, size):
        self.name = name
        self.crop_yield = crop_yield
        self.status = status
        self.water_need = water_need
        self.temp_need = temp_need
        self.pest_resist = pest_resist
        self.size = size
    