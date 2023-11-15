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

    # Line 4-7: Determine time and location based on completion time
    # n_job이 끝날 때 까지 내려간다. X또는 2*X 시간으로 행을 끊어서 얻어진 행의 min(t,l)을 구하고 리스트에 쌓는다.
    if X < 24 * 7: # one week:
    else:

    # Line 9: Sort list based on time values
    # (t,l)이 쌓인 리스트를 정렬

    # Line 10-17: Apply scheduling based on conditions
    for t, l in (t,l)이 쌓인 list:
        if l_j == l_(j+1) and t_(j+1) != t_j + 1:
            apply_suspend_resume()
        elif l_j != l_(j+1) and t_(j+1) == t_j + 1:
            apply_moving_between_clouds()
        elif l_j != l_(j+1) and t_(j+1) != t_j + 1:
            apply_moving_between_clouds_and_suspend_resume()

# 필요 함수 정의
def all_possible_locations(job):
  # job에 location category가 존재하는가? # 1번 열 이라면
  # return np.uniquie(job[1]))
  return 0

def minimum_completion_time(job):
  # job에 time category가 존재하는가? # 0번 열 이라면
  # return min(job[0], axis=0)
  return 0

def get_num_epochs(job):
  return 0

def n_job(job, num_epochs):
  # 주어진 배열을 복사
  c_job = np.copy(job)

  # 복사한 배열을 n-1번 추가하여 쌓음
  n_job = np.vstack([job] * (num_epochs-1) + [c_job])

  return n_job

def apply_suspend_resume():
  return 0

def apply_moving_between_clouds():
  return 0

def apply_moving_between_clouds_and_suspend_resume():
  return 0