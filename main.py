def findRootsOfQuadratic(a, b, c):
  """
  This function finds the roots of a quadratic equation (y = ax^2 + bx + c)
  """
  d = b ** 2 - 4 * a * c
  
  if d < 0:
    return "No real roots"
  
  if d == 0:
    x1 = -b / (2 * a)
    x2 = x1
    return (x1, x2)
  
  if d > 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    return (x1, x2)