
import random

SID_RAND_PART_LEN = 14

def main():
  nums = []
  for i in range(10000):
    rnum = generateSecId()
    if rnum not in nums:
      nums.append(rnum)
  print len(nums)

def generateSecId():
  secID = ""
  random.seed()
  for i in range(SID_RAND_PART_LEN):
    r = random.random()
    r = r * 25
    if r >= 14:
      r = r + 1
    secID = secID + chr(65 + int(r))
  return secID

if __name__ == "__main__":
    main()
