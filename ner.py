import math

class Neuron:
    def __init__(self):
        pass

    def calculate_quadratic_equation(self, a, b, c):
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            return root1, root2
        elif discriminant == 0:
            root = -b / (2*a)
            return root
        else:
            return "Complex Roots"

neuron = Neuron()
a, b, c = 1, -3, 2  # Пример коэффициентов квадратного уравнения x^2 - 3x + 2
roots = neuron.calculate_quadratic_equation(a, b, c)
print(roots)