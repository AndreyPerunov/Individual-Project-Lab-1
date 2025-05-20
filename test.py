from main import findRootsOfQuadratic
import json

with open('input.json') as f:
  data = json.load(f)

with open('expected.json') as f:
  expected = json.load(f)

test_results = []
results = []

for i in range(len(data)):
  a = data[i]['a']
  b = data[i]['b']
  c = data[i]['c']
  error = expected[i]['error']
  if len(error) == 0:
    [x1, x2] = findRootsOfQuadratic(a, b, c)
    result = f"{i} Test passed" if (round(x1, 4), round(x2, 4)) == (round(expected[i]['x1'], 4), round(expected[i]['x2'], 4)) else f"{i} Test failed"
    test_results.append(result)
    results.append((x1, x2))
  else:
    realError = findRootsOfQuadratic(a, b, c)
    result = f"{i} Test passed" if realError == error else f"{i} Test failed"
    test_results.append(result)
    results.append(realError)
    
# write test results to a file
with open('test_results.txt', 'w') as f:
  for result in test_results:
    f.write(result + '\n')

# write results to a file
with open('results.txt', 'w') as f:
  for result in results:
    f.write(str(result) + '\n')