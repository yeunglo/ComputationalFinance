#!python3
# coding:gbk

print('what\'s your name��').decode("utf-8")
name = input()
print('�������ϴ�����:(ǧ��)')
s1 = float(input())
print("������������:(ǧ��)")
s2 = float(input())
print('�������ǣ�(��)')
s3 = float(input())
r1 = (s2-s1)/s1*100
r2 = s2/(s3*s3)
print('hello!%s'%name)
if s1 > s2:
    print('������ؼ�����%.1f%%'%(-r1))
elif s1 == s2:
    print('�㻹����ô��')
else:
    print('�������������%.1f%%'%(r1))
if r2 < 18.5:
    print('���BMIָ����%.1f'%(r2),',�ݱ�')
elif r2<25:
    print('���BMIָ����%.1f'%(r2),',����').decode("utf-8")
elif r2<28:
    print('���BMIָ����%.1f'%(r2),',�е㳬��')
elif r2<32:
    print('���BMIָ����%.1f'%(r2),',С����')
else:
    print('���BMIָ����%.1f'%(r2), ',������')