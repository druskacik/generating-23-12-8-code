from itertools import permutations

biplane = [
  '13459','2456X', '35670', '46781',
  '57892', '689X3', '79X04', '8X015',
  '90126', 'X1237', '02348'
]

s = '0123456789X'

def hamming(a, b):
  d = 0
  for i in range(len(a)):
    if a[i] != b[i]:
      d += 1
  return d

def identity(n):
  mat = []
  for i in range(n):
    row = [0 for j in range(n)]
    row[i] = 1
    mat.append(row)
  return mat

def create_incidence_matrix(blocks, elements):
  matrix = []
  for block in blocks:
    row = []
    for e in elements:
      row.append(1 if e in block else 0)
    matrix.append(row)
  return matrix

def create_code_matrix():
  m = create_incidence_matrix(biplane, s)
  m.append([1 for i in range(11)])
  I = identity(12)
  matrix = []
  for i in range(12):
    # row = I[i] + [1] + m[i]
    row = I[i] + m[i]
    matrix.append(row)
  # matrix[11][12] = 0
  return matrix

def create_codewords(matrix):
  codewords = []
  for row in matrix:
    c = ''
    for v in row:
      c += str(v)
    codewords.append(c)
  return codewords

def minimum_distance(code):
  distances = []
  for p in permutations(code, 2):
    distances.append(hamming(p[0], p[1]))
  return min(distances)

matrix = create_code_matrix()
code = create_codewords(matrix)

# will be 8 ! 
minimum = minimum_distance(code)
print(minimum)

# print(len(code[0]))
# print(len(code))

# for codeword in code:
#   print(codeword)
