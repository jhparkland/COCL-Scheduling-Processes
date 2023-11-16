# COCL-Scheduling-Processes
COCL timetable scheduling using genetic algorithm, etc.

## 프로젝트 목표
태양광 발전이 최대인 시간대에 GPU,TPU를 사용하는 수업을 배치하는 것.

- 탄소발자국 정보가 포함된 강의 정보 모델(/클래스 및 속성 개발) 예로, class Lecture, class CarbonFootPrint
- 일자/시간별 태양광발전 모델을 구성, class PVGeneration
- 탄소발자국 정보을 가진 강의와 태양광 발전 정보를 가지고 Net-zero를 극대화할 수 있는 강의 스케쥴러 구성 (학기마다), class NetZeroScheduler

## 추가설명
Net-zero equation = production energy(PE) - used energy(UE) =~ 0에 근접
만약 1시-2시의 강의가 = 100kw(PE) - 80kw(UE) = 20 이라면 20가 비효율적임.
만약 1시-2시의 강의가 = 100kw(PE) - 120kw(UE) = -20 이라면 20정도의 전력이 부족(이건 중앙 전력/계통의 전력을 사용함), 혹은 추가적인 설치가 필요

## 개발 사항
- 뼈대 Code 제작
- 필요 함수 부분 정의 필요
- 4번 라인부터 추가 작업 필요

## 참여 신청 방법

1. issues 탭 클릭
2. new issues 클릭 후 가입신청 템플릿 선택
3. 양식에 맞춰 작성
