def findRootsOfQuadratic(a, b, c): 
  """
  This function finds the roots of a quadratic equation (y = ax^2 + bx + c)
  """
  d = b ** 2 - 4 * a * c #1
  
  if d < 0: #2
    return "No real roots" #3
  elif d == 0: #4
    x1 = -b / (2 * a) #5
    x2 = x1 #6
    return (x1, x2) #7
  else:
    x1 = (-b + d ** 0.5) / (2 * a) #8
    x2 = (-b - d ** 0.5) / (2 * a) #9
    return (x1, x2) #10
#11