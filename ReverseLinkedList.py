#So you set a current, current = head, set prev to the node behind current, initially None
#Then current.next = prev, then move the iteration forward by prev = current and current now = temp

current = head
prev = 0

while current: 
  temp = current.next
  current.next = prev
  prev = current
  current = temp
return prev
