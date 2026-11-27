class Body:
    def __init__(self, mass, heat_capacity, temp):
        self.mass = mass
        if mass <= 0:
            print("Mass has to be bigger than 0 ")
        self.heat_capacity = heat_capacity
        if heat_capacity <= 0:
            print("Heat capacity has to be bigger than 0")
        self.temp = temp
        if temp < 0:
            print("Temperature has to be 0 or positive")

    def add_heat(self, heat):
        d_temp = heat / (self.mass * self.heat_capacity)
        self.temp += d_temp
        return self.temp


if __name__ == "__main__":
    b = Body(mass = 100, heat_capacity = 0.15, temp = 200)
    temp_1 = b.add_heat(20)
    print(temp_1)
    temp_2 = b.add_heat(-40)
    print(temp_2)


