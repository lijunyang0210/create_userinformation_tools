import basic_tool.tool

# 姓名
# 性别
# 邮箱
# 电话
# 地址
sex = basic_tool.tool.get_sex()
name = basic_tool.tool.get_name(sex)
email = basic_tool.tool.get_email()
telephone = basic_tool.tool.get_email()
addr = basic_tool.tool.get_addr()

print(sex, name, email, telephone, addr)
