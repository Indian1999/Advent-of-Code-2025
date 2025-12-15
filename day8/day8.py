import os
import numpy as np

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2) ** 0.5
    
    def __str__(self):
        return f"({self.x},{self.y},{self.z})"
    
class Circuit:
    def __init__(self, points = []):
        self.points = points

    def __iadd__(self, point):
        self.points.append(point)

    def distance_to(self, other):
        """single linkage"""
        min_distance = float("inf")
        for a in self.points:
            for b in other.points:
                distance = a.distance_to(b)
                if distance < min_distance:
                    min_distance = distance
        return min_distance
    
    def __add__(self, other):
        return Circuit(self.points + other.points)
    
    def __len__(self):
        return len(self.points)
    
    def __contains__(self, point):
        return point in self.points
    
    def __str__(self):
        output = ""
        for point in self.points:
            output += str(point) + ", "
        return output[:-2]
    
class Space:
    def __init__(self, path):
        self.circuits = []
        self.points = []
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip().split(",")
                line = [int(item) for item in line]
                point = Point(*line)
                self.circuits.append(Circuit([point]))
                self.points.append(point)

    def __str__(self):
        output = ""
        for circuit in self.circuits:
            output += str(circuit) + "\n"
        return output

    def top_n_shortest_distances(self, n):
        distances = {}
        for i in range(len(self.points)):
            for j in range(i+1, len(self.points)):
                distances[(i,j)] = self.points[i].distance_to(self.points[j])
        distances = sorted(list(distances.items()), key = lambda x: x[1], reverse=False)
        return distances[:n]
        
    def __iadd__(self, circuit:Circuit):
        self.circuits.append(circuit)

    def closest_circuit_ids(self):
        min_distance = float("inf")
        min_ids = None
        for i in range(len(self.circuits)):
            for j in range(i + 1, len(self.circuits)):
                distance = self.circuits[i].distance_to(self.circuits[j])
                if distance < min_distance:
                    min_distance = distance
                    min_ids = (i, j)
        return min_ids

    def merge_two_circuits(self, i, j):
        self.circuits[i] = self.circuits[i] + self.circuits.pop(j)

    def is_same_circuit(self, a, b):
        for i in range(len(self.circuits)):
            if a in self.circuits[i] and b in self.circuits[i]:
                return True
        return False
    
    def get_circuit_by_point(self, point):
        for i in range(len(self.circuits)):
            if point in self.circuits[i]:
                return i
        raise Exception(f"{point} is not in any of the circuits")


    def merge_circuits(self, n_merges = float("inf")):
        merge_counter = 0
        closest_points = self.top_n_shortest_distances(n_merges)
        while merge_counter < n_merges:
            a, _ = closest_points[merge_counter]
            if not self.is_same_circuit(self.points[a[0]], self.points[a[1]]):
                self.merge_two_circuits(
                    self.get_circuit_by_point(self.points[a[0]]),
                    self.get_circuit_by_point(self.points[a[1]])
                )
            merge_counter += 1

    def calculate_value(self):
        self.merge_circuits(n_merges = 10)
        self.circuits.sort(key = lambda x: len(x), reverse=True)
        value = 1
        for i in range(3):
            value *= len(self.circuits[i])
        return value


PATH = os.path.join(os.path.dirname(__file__), "day8_1.txt")
space = Space(PATH)
print(space.calculate_value())


# WRONG for part1: 8