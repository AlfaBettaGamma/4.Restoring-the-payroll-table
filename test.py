def  SynchronizingTables(N, ids, salary):
  new_ids = []
  new_salary = []
  if len(ids) == len(salary) == N:
    for i in range(len(ids)):
      new_ids.append(ids[i])
      new_salary.append(new_salary[i])
    for i in range(len(new_salary) - 1):
      for j in range(len(new_salary) - i - 1):
        if new_ids[j] < new_ids[j + 1] :
          new_ids[j], new_ids[j + 1] = new_ids[j + 1], new_ids[j]
          new_salary[j], new_salary[j + 1] = new_salary[j + 1], new_salary[j]
    return new_salary
  else:
    return print("Неверное значение!")
  

def test1():
  SynchronizingTables(3,[50,1,1024],[20000,100000,90000])

def test2():
  SynchronizingTables(2,[50,1,1024],[20000,100000,90000])

def test3():
  SynchronizingTables(3,[50,1,1024],[20000,100000,90000,2000])

