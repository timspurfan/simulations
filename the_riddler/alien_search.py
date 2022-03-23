'''

Problem: 2 aliens and 1 policeman are randomly placed on a planet.  The policeman moves
20x faster than the aliens.  What is the probability that the aliens rendezvous before
the policeman is able to get there.

used:https://www.cs.cmu.edu/~mws/rpos.html

'''

from tqdm import tqdm
import random
import numpy as np
import math

results = []
num_trials = 10**5

def generate_random_coords():

    z = random.uniform(-1,1)
    phi = random.uniform(0, 2*math.pi) #longitude
    theta = math.asin(z) #latitude
    lat = theta
    long = phi
    x = math.cos(theta)*math.cos(phi)
    y = math.cos(theta)*math.sin(phi)

    return(x,y,z,lat,long)

def get_lat(rectangular_coords):

    x,y,z = rectangular_coords

    if x > 0:
        return math.atan(y/x)
    if y > 0:
        return math.atan(y/x)+math.pi

    return math.atan(y/x)-math.pi

def midpoint_coords(coords1, coords2):
    x1, x2 = coords1[0],coords2[0]
    y1, y2 = coords1[1],coords2[1]
    z1, z2 = coords1[2],coords2[2]

    mid = np.array(((x1+x2)/2,(y1+y2)/2,(z1+z2)/2))
    magnitude = math.sqrt(np.dot(mid,mid))
    if magnitude == 0:
        raise ValueError
    #STILL HAVE CASE IF MAGNITUDE = 0
    normalized_mid = (1/magnitude)*mid
    long = math.asin(normalized_mid[2])
    lat = get_lat(tuple(normalized_mid))
    l = [lat,long]
    normalized_mid = np.append(normalized_mid,l)
    return tuple(normalized_mid)

def haversine_distance(p1,p2):

    lat1, lon1 = p1[3],p1[4]
    lat2, lon2 = p2[3],p2[4]

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)

    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    return c

for trial in tqdm(range(num_trials)):

    policeman_coords = generate_random_coords()
    alien1_coords = generate_random_coords()
    alien2_coords = generate_random_coords()

    rendezvous_point = midpoint_coords(alien1_coords, alien2_coords)
    
    d_aliens = haversine_distance(alien1_coords, rendezvous_point)
    d_police = haversine_distance(policeman_coords, rendezvous_point)

    if d_police < 20*d_aliens:
        #police will catch them
        results.append(1)
    else:
        #aliens will rendezvous
        results.append(0)
    
probability = np.mean(results)
print(probability)