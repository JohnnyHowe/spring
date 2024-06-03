from vector2 import Vector2


class Spring2D:

    def __init__(self, spring_force=3, damping_factor=1):
        self.spring_force = spring_force
        self.damping_factor = damping_factor

        self.postion = Vector2(0, 0)
        self.target = Vector2(0, 0)
        self.velocity = Vector2(0, 0)

    def update(self, delta_time):

        distance_to_target = self.target - self.postion
        spring_force = distance_to_target * self.spring_force

        damp_force = self.velocity * -1 * self.damping_factor

        self.velocity += (spring_force + damp_force) * delta_time
        self.postion += self.velocity * delta_time

    def set_target(self, new_target):
        self.target = new_target
