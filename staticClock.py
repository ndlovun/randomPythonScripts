#Write a function, which takes a non-negative integer (seconds) as input and returns the time in a
#human-readable format (HH:MM:SS) Test.assert_equals(make_readable(86399), "23:59:59")
num = 86399
#num = 5

if num >= 3600:
    rtrnLst=(num//3600,(num%3600)//60,(num%3600)%60)

elif num >= 60:
    rtrnLst=('00:'+str(num//60)+':'+str((num%3600)%60))

elif num < 60 and num >= 10:
    rtrnLst=('00:00:'+str(num))
    #rtrnLst.append(num)
else:
    rtrnLst=('00:00:0'+str(num))

print(rtrnLst)
