import numpy as np

# The scheduling procedure of SR(Suspend Resume)&MBC(Moving between Clouds)

def schedule(jobs):
  for i in range(0, len(jobs)):
    job = jobs[i]
    # Line 1 : all the possible locations
    L = all_possible_locations(job)
    # Line 2 : minimum job completion time
    X = minimum_completion_time(job)
    # Line 3 : number of epochs of the training porcess
    num_epochs = get_num_epochs(job)

    # 에포크수만큼의 job
    n_job = n_job(job, num_epochs)

    # Line 4-8: Determine time and location based on minimum values of CO2
    if X < 24 * 7: # one week # 2*X
      target_time = 2 * X
    else: # over the one week # X
      target_time = X

    t_l_list = time_location_list(n_job, target_time)

    # Line 9: Sort t_l_list based on time values / (t, l) 중 t의 값에 따라 정렬
    t_l_list = sorted(t_l_list, key=lambda x: float(x[0]))
    
    # Line 10-18: Apply scheduling based on conditions / (t, l): t- t_l_list[0], l- t_l_list[1]
    for i in range(len(t_l_list) - 1): # i+1에 접근하기 때문에 -1 처리
      if t_l_list[i][1] == t_l_list[i+1][1] and t_l_list[i+1][0] != t_l_list[i][0] + 1: # 현재 location과 다음 location이 같고, 현재 time+1과 다음 time과 다를 때
        suspend_resume() # 일시중지, 다시시작
      elif t_l_list[i][1] != t_l_list[i+1][1] and t_l_list[i+1][0] == t_l_list[i][0] + 1: # 현재 location과 다음 location이 다르고, 현재 time+1과 다음 time과 같을 때
        moving_between_clouds() # 클라우드로 옮기기
      elif t_l_list[i][1] != t_l_list[i+1][1] and t_l_list[i+1][0] != t_l_list[i][0] + 1: # 현재 location과 다음 location이 다르고, 현재 time+1과 다음 time과 다를 때
        suspend_resume() # 일시중지, 다시시작
        moving_between_clouds() # 클라우드로 옮기기

# 필요 함수 정의
def all_possible_locations(job):
  # job에 location category가 존재하는가? # 1번 열 이라면
  return np.uniquie(job[1])

def minimum_completion_time(job):
  # job에 time category가 존재하는가? # 0번 열 이라면
  return min(job[0], axis=0)

def get_num_epochs(job):
  # 에포크 수 정하기
  return 0

def n_job(job, num_epochs):
  # 주어진 배열을 복사
  c_job = np.copy(job)

  # 복사한 배열을 n-1번 추가하여 쌓음
  n_job = np.vstack([job] * (num_epochs-1) + [c_job])

  return n_job

def time_location_list(n_job, target_time):
  # n_job이 끝날 때 까지 반복. target_time(2*X또는 X시간)으로 행을 끊어서, 얻어진 행 중 CO2가 가장 작은 행의 (t,l)을 구하고 리스트에 쌓음
  t_l_list = []

  while len(n_job) > 0:
    current_sum = 0
    row_indices = []
    
    for i, row in enumerate(n_job): #target_time이 넘지 않을 때까지 반복
      # 0번 열(time)의 값을 숫자(실수)로 변환하여 현재 합에 더하기
      current_sum += float(row[0])
      
      # current_sum이 target_time를 넘지 않으면 행 번호를 리스트에 추가
      if current_sum <= target_time:
        row_indices.append(i)
      # 넘으면 반복문 탈출
      else:
        break

    # row_indices에 해당하는 행들 중 2번 열(CO2)이 가장 작은 행을 찾음
    min_row_index = min(row_indices, key=lambda x: n_job[x, 2])
    
    # 해당 행의 0번 열(time)과 1번 열(location)을 튜플로 묶어서 반환
    t_l_tuple = (n_job[min_row_index, 0], n_job[min_row_index, 1])
    
    # t_l_list에 반환 받은 t_l_tuple 추가
    t_l_list.append(t_l_tuple)
    
    # row_indices 해당하는 행을 삭제
    n_job = np.delete(n_job, row_indices, axis=0)
    
  return t_l_list

def suspend_resume():
  # 일시중지, 다시시작
  return 0

def moving_between_clouds():
  # 클라우드로 옮기기
  return 0
