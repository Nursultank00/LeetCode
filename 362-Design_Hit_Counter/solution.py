times = []
hits = []
 
for i in range(0,300):
  times.append(0)
  hits.append(300)
 
''' Record a hit.
@param timestamp - The current timestamp
(in seconds granularity). '''
def hit(timestamp):
  idx = timestamp % 300
  if (times[idx] is not timestamp):
    times[idx] = timestamp
    hits[idx] = 1
  else:
    hits[idx]+=1
 
# Time Complexity : O(1)
 
''' Return the number of hits in the past 5 minutes.
    @param timestamp - The current timestamp (in
    seconds granularity). '''
def getHits(timestamp):
  res = 0
  for i in range(0,300):
    if (timestamp - times[i] < 300):
      res += hits[i]
  return res
 
# Time Complexity : O(300) == O(1)