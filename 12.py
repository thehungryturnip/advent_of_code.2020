#!/usr/bin/env python3

from time import perf_counter

class Ship():
    def __init__(self):
        self.reset()

    def reset(self):
        self.lon = 0
        self.lat = 0
        self.degree = 0

        self.wp_lon = 10
        self.wp_lat = 1

    def move(self, a, v):
        DEG_TO_DIR = {
            0: 'E',
            90: 'S',
            180: 'W',
            270: 'N',
        }
        if a == 'N':
            self.lat += v
        if a == 'S':
            self.lat -= v
        if a == 'E':
            self.lon += v
        if a == 'W':
            self.lon -= v
        if a == 'F':
            self.move(DEG_TO_DIR[self.degree], v)
        if a == 'R':
            self.degree += v
            self.degree %= 360
        if a == 'L':
            self.degree -= v
            self.degree %= 360

    def waypoint_move(self, a, v):
        if a == 'N':
            self.wp_lat += v
        if a == 'S':
            self.wp_lat -= v
        if a == 'E':
            self.wp_lon += v
        if a == 'W':
            self.wp_lon -= v
        if a == 'F':
            self.lat += v * self.wp_lat
            self.lon += v * self.wp_lon
        if a == 'R':
            for t in range(v // 90):
                self.rotate_waypoint(True)
        if a == 'L':
            for t in range(v // 90):
                self.rotate_waypoint(False)

    def rotate_waypoint(self, clockwise):
        if clockwise:
            self.wp_lon, self.wp_lat = self.wp_lat, -self.wp_lon
        else:
            self.wp_lon, self.wp_lat = -self.wp_lat, self.wp_lon

    def distance(self):
        return abs(self.lon) + abs(self.lat)

instructions = []
with open('12.in', 'r') as f:
    for l in f:
        action = l[0]
        value = int(l[1:])
        instructions.append((action, value))

tic = perf_counter()
s = Ship()
for i in instructions:
    s.move(*i)
toc = perf_counter()
print(f'[12a] The position of the ship is ({s.lon},{s.lat}) with a distance of '
      f'{s.distance()}. ({toc - tic})')

tic = perf_counter()
s.reset()
for i in instructions:
    s.waypoint_move(*i)
toc = perf_counter()
print(f'[12b] The position of the ship is ({s.lon},{s.lat}) with a distance of '
      f'{s.distance()}. ({toc - tic})')
