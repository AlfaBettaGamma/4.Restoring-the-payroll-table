def  SynchronizingTables(N, ids, salary):
  new_ids = []
  if len(ids) == len(salary) == N:
    for i in range(len(ids)):
      new_ids.append(ids[i])
    for i in range(len(salary) - 1):
      for j in range(len(salary) - i - 1):
        if new_ids[j] < new_ids[j + 1] :
          new_ids[j], new_ids[j + 1] = new_ids[j + 1], new_ids[j]
          salary[j], salary[j + 1] = salary[j + 1], salary[j]
    return salary
  else:
    print("Неверное значение!")