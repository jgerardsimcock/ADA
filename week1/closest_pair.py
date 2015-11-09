from merge_sort_2d import *
#We need these to test our algos
import math, random, re


def pre(points):
  """We pre-process the set of points and order them along their x and y axis"""

  px = merge_sort_2d(points, 0)
  py = merge_sort_2d(points, 1)
  return px, py

#pre works

def distance(pair):
  """Calculate Euclidean distance between two points."""

  try: 
      a,b = pair[0], pair[1]
      return math.sqrt((a[0]- b[0])**2 + (a[1] - b[1])**2)

  except:
      return None

#distance works


def closest_split_pair(Px, Py, delta):
  """Return possible point pair whose distance is less than delta. This
  function is needed when the two closest points have been split 
  between two arrays"""


  #Split the length of Px 
  mid = int(len(Px)/2)

  x_bar = Px[mid-1][0]#biggest x-coordinate in left of P
  bar_pts = [p for p in Py if ((x_bar - delta) <= p[0] <= (x_bar + delta))]

  best = delta
  best_pair = None

  for i in range(0, len(bar_pts)):
    for j in range(0, min(7, len(bar_pts)-i)):
      if i == (i+j): #this checks to make sure we are not double counting
          continue

      pair = [bar_pts[i], bar_pts[i+j]]

      if distance(pair) < best:
        best_pair = pair
        best = distance(pair)


  return best_pair

def closest_pair(Px, Py):
  """Best case scenario: return point pairs whose distance is less than delta"""

  mid = int(len(Px)/2)

  left_x = Px[:mid]
  right_x = Px[mid:]
  left_y = Py[:mid]
  right_y = Py[mid:]
  pair_distance = []

  #We need a base case  
  if len(Px) == 1:
    return None

  elif len(Px) == 2:
    return Px

  else:
    left = closest_pair(left_x, left_y)
    right = closest_pair(right_x, right_y)
    #if None is in (left,right)

    if left == None:
      delta = distance(right)

    else:
      delta = min(distance(left), distance(right))

    split = closest_split_pair(Px,Py,delta)

    pair_distance = [(x, distance(x)) for x in (left, right, split) if x]

    return merge_sort_2d(pair_distance, 1)[0][0]


def closestPair_helper(points):
    """pre-sorts, runs closest pair and returns closest pair"""

    Px, Py = pre(points)

    return closest_pair(Px, Py)


#test this out

# pts = [(1,4), [7,0], [1,2], [0,0]]

# print closestPair_helper(pts)

#random.seed(3)

rand_pts = []
for i in range(100):
  a, b = random.randint(0,100), random.randint(0,100)

  if (a,b) not in rand_pts:
    rand_pts.append((a,b))

print closestPair_helper(rand_pts)




