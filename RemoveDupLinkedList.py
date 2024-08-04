# so you set cur = head
# do a loop, check if cur.val == cur.next.val, if it's equal, change the nxtnxt, if not, change iterate fwd

cur = head 
while cur and cur.next:
  if cur.val == cur.next.val:
    cur.next = cur.next.next
  else:
    cur = cur.next
return head

