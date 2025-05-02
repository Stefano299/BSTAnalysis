
  
  def insertTest(startN, endN, step, maxN):
  sizes = list(range(startN, endN, step))
  trials = 5
  """
  tempi1 = []
  for n in sizes:
    run_times = []
    for _ in range(trials):
      standardABR = StandardABR()
      t = measureTime(standardABR.addNodes, n, maxN)
      run_times.append(t)
    tempi1.append(sum(run_times) / trials)
  """
  tempi3 = []
  for n in sizes:
    run_times = []
    for _ in range(trials):
      listABR = ListABR()
      t = measureTime(listABR.addNodes, n, maxN)
      run_times.append(t)
    tempi3.append(sum(run_times) / trials)

  tempi2 = []
  for n in sizes:
    run_times = []
    for _ in range(trials):
      flagABR = FlagABR()
      t = measureTime(flagABR.addNodes, n, maxN)
      run_times.append(t)
    tempi2.append(sum(run_times) / trials)

  # Smoothing con media mobile
  def moving_average(data, window=5):
      half = window // 2
      smoothed = []
      for i in range(len(data)):
          start = max(0, i - half)
          end = min(len(data), i + half + 1)
          smoothed.append(sum(data[start:end]) / (end - start))
      return smoothed

  #tempi1 = moving_average(tempi1)
  tempi2 = moving_average(tempi2)
  tempi3 = moving_average(tempi3)

  createAndShowPlt(
    sizes, tempi2, 'Size', 'Tempo di inserimento (s)',
    'Tempo di inserimento in ABR1 vs ABR2 vs ABR3',
    label1='ABR1', yArr2=tempi3, label2='ABR2',
  )
  
def insert1Test(startN, endN, step, maxN):
  sizes = list(range(startN, endN, step))
  trials = 1
  """
  tempi1 = []
  for n in sizes:
    run_times = []
    for _ in range(trials):
      standardABR = StandardABR()
      t = measureTime(standardABR.addNodes, n, maxN)
      run_times.append(t)
    tempi1.append(sum(run_times) / trials)
  """
  tempi3 = []
  listABR = ListABR()
  for n in sizes:
    run_times = []
    for _ in range(trials): 
      node = Node(random.randint(1, maxN))
      t = measureTime(listABR.insert, node)
      run_times.append(t)
    tempi3.append(sum(run_times) / trials)

  tempi2 = []
  flagABR = FlagABR()
  for n in sizes:
    run_times = []
    for _ in range(trials): 
      node = Node(random.randint(1, maxN))
      t = measureTime(flagABR.insert, node)
      run_times.append(t)
    tempi2.append(sum(run_times) / trials)

  # Smoothing con media mobile
  def moving_average(data, window=5):
      half = window // 2
      smoothed = []
      for i in range(len(data)):
          start = max(0, i - half)
          end = min(len(data), i + half + 1)
          smoothed.append(sum(data[start:end]) / (end - start))
      return smoothed

  #tempi1 = moving_average(tempi1)
  tempi2 = moving_average(tempi2)
  tempi3 = moving_average(tempi3)

  createAndShowPlt(
    sizes, tempi2, 'Size', 'Tempo di inserimento (s)',
    'Tempo di inserimento in ABR1 vs ABR2 vs ABR3',
    label1='ABR1', yArr2=tempi3, label2='ABR2',
  )
  
def insert1Test(startN, endN, step, maxN):
  sizes = list(range(startN, endN, step))
  trials = 1
  tempi2, tempi3 = [], []  # timings for FlagABR, ListABR

  for n in sizes:
      # FlagABR
      flag_times = timeit.repeat(lambda: FlagABR().addNodes(n, maxN), repeat=trials, number=1)
      tempi2.append(min(flag_times))
      # ListABR
      list_times = timeit.repeat(lambda: ListABR().addNodes(n, maxN), repeat=trials, number=1)
      tempi3.append(min(list_times))

  # Smoothing con media mobile
  def moving_average(data, window=5):
      half = window // 2
      smoothed = []
      for i in range(len(data)):
          start = max(0, i - half)
          end = min(len(data), i + half + 1)
          smoothed.append(sum(data[start:end]) / (end - start))
      return smoothed

  tempi2 = moving_average(tempi2)
  tempi3 = moving_average(tempi3)

  createAndShowPlt(
    sizes, tempi2, 'Size', 'Tempo di inserimento (s)',
    'Confronto tempi inserimento: Flag vs List',
    label1='FlagABR', yArr2=tempi3, label2='ListABR'
  )
  
  def computeMaxNum(n, dupRate):
  frac_dups = dupRate / 100.0
  target_unique = n * (1 - frac_dups)

  low, high = 1.0, float(n)
  while high * (1 - (1 - 1/high)**n) < target_unique:
    high *= 2

  for _ in range(30):
    mid = (low + high) / 2.0
    expected_unique = mid * (1 - (1 - 1/mid)**n)
    if expected_unique > target_unique:
      high = mid
    else:
      low = mid

  return math.ceil(high)