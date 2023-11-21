import numpy as np

# The scheduling procedure of SR(Suspend Resume)&MBC(Moving between Clouds)

def schedule(jobs):
  # Line 1 : all the possible locations
  #L = all_possible_locations(jobs)
  # Line 2 : minimum jobs completion time
  #X = minimum_completion_time(jobs)
  # Line 3 : number of epochs of the training porcess
  num_epochs = 15 # 15주 수업

  # Line 4-9: Determine time and location based on minimum values of CO2, Sort list
  order = np.lexsort((jobs[:, 0], jobs[:, 2]))
  jobs = jobs[order]

  SR_MBC_list = []

  # Line 10-18: Apply scheduling based on conditions / t- jobs[0], l- jobs[1] # 일단 jobs 원소와 순서를 맞춘 SR, MBC여부를 나타낸 리스트를 만듦, 즉 해당 수업에서 어떤 일을 해야할지 리스트로 나옴
  for i in range(len(jobs) - 1): # i+1에 접근하기 때문에 -1 처리
    if jobs[i][1] == jobs[i+1][1] and jobs[i][0] < 1.5: # 현재 강의 위치와 다음 강의 위치가 같고, 현재 강의 시간이 1.5시간보다 적을 때
      SR_MBC_list = suspend_resume(SR_MBC_list) # 일시중지, 다시시작
    elif jobs[i][1] != jobs[i+1][1] and jobs[i][0] > 1.5: # 현재 강의 위치와 다음 강의 위치가 다르고, 현재 강의 시간이 1.5시간보다 많을 때
      SR_MBC_list = moving_between_clouds(SR_MBC_list) # 클라우드로 옮기기
    elif jobs[i][1] == jobs[i+1][1] and jobs[i][0] > 1.51: # 현재 강의 위치와 다음 강의 위치가 같고, 현재 강의 시간이 1.5시간보다 많을 때
      SR_MBC_list = sr_mbc(SR_MBC_list) # 일시중지, 클라우드로 옮기기, 다시시작
    else:
      SR_MBC_list.append(" ")
  
  SR_MBC_list.append(" ") # 마지막 수업에 공백으로 채우면서 수업 개수 맞추기
  SR_MBC_list = np.array(SR_MBC_list)

  np.insert(jobs, -1, SR_MBC_list, axis=1) # jobs의 마지막 열로 SR_MBC_list 추가

  # 15주 수업 반복
  n_jobs = n_jobs(jobs, num_epochs)
return n_jobs

# 필요 함수 정의 #
def all_possible_locations(jobs):
  # job에 location category가 존재하는가? # 1번 열 이라면
  return np.uniquie(jobs[1])

def minimum_completion_time(job):
  # job에 time category가 존재하는가? # 0번 열 이라면
  return jobs[0].sum(axis=0)

def suspend_resume(SR_MBC_list):
  # 일시중지, 다시시작
  SR_MBC_list.append("SR")
  return SR_MBC_list

def moving_between_clouds(SR_MBC_list):
  # 클라우드로 옮기기
  SR_MBC_list.append("MBC")
  return SR_MBC_list

def sr_mbc(SR_MBC_list):
  # 일시중지, 클라우드로 옮기기, 다시시작
  SR_MBC_list.append("SR, MBC")
  return SR_MBC_list

def n_jobs(jobs, num_epochs):
  # 주어진 배열을 복사
  c_jobs = np.copy(jobs)

  # 복사한 배열을 n-1번 추가하여 쌓음
  n_jobs = np.vstack([jobs] * (num_epochs-1) + [c_job])

  return n_jobs
