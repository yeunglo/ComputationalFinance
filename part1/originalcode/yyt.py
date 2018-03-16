#!python3
# coding:gbk

print('what\'s your name？').decode("utf-8")
name = input()
print('请输入上次体重:(千克)')
s1 = float(input())
print("请输出这次体重:(千克)")
s2 = float(input())
print('你的身高是：(米)')
s3 = float(input())
r1 = (s2-s1)/s1*100
r2 = s2/(s3*s3)
print('hello!%s'%name)
if s1 > s2:
    print('你的体重减少了%.1f%%'%(-r1))
elif s1 == s2:
    print('你还是这么胖')
else:
    print('你的体重增加了%.1f%%'%(r1))
if r2 < 18.5:
    print('你的BMI指数是%.1f'%(r2),',瘦逼')
elif r2<25:
    print('你的BMI指数是%.1f'%(r2),',正常').decode("utf-8")
elif r2<28:
    print('你的BMI指数是%.1f'%(r2),',有点超重')
elif r2<32:
    print('你的BMI指数是%.1f'%(r2),',小胖子')
else:
    print('你的BMI指数是%.1f'%(r2), ',死胖子')