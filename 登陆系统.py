database = {'a': '1', 'b': '2','c':'3','d':'4','e':'5'}

print('登陆')
while True:
    name = input('请输入您的用户名：')
    if name in database:
        break
    else:
        print('您输入的用户名不存在，请重新输入')
i=0 
while i<5:
    password = input('请输入您的密码：')
    if database[name] == password:
        print('欢迎您，%s'%(name))
        break
    elif password == "":
        print('密码不能为空，请重新输入密码')
    else:
        i=i+1;
        print('您输入的密码不正确，还有%d次输入机会'%(5-i))
else:
    print("您的账户已锁定，无法继续输入")

