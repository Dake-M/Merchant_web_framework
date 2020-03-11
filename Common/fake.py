# -*- coding: utf-8 -*-
# @Project  :merchant_web_framework
# @File     :fake
# @Date     :2020/3/11 10:27
# @Author   :Dake
# @Email    :6004297158@qq.com
# @Software :PyCharm
from faker import Faker


class fake:
    """
    这是一个随机构造测试数据的功能封装
    """

    """
    Python：随机生成测试数据的模块--faker
    pip3 install Faker
    【使用faker也能识别成功，不过新版已经更新为Faker】
    from faker import Faker
    【主要使用的是Factory类，而导入Faker，会同时导入Factory】
    使用步骤：
        初始化：fake=Faker()
        调用方法: 利用Faker对象调用方法，调用方法的返回值就是随机的数据。不同的数据需要调用不同的方法，常见方法参见下面。
            from faker import Faker

            # fake=Faker() #默认生成美国英文数据
            fake=Faker(locale='zh_CN')

            # 地址类
            print("地址类".center(20,"-"))
            print(fake.address())#海南省成市丰都深圳路p座 425541
            print(fake.street_address())#深圳街X座
            print(fake.street_name())#长沙路
            print(fake.city_name(),fake.city())#兰州 贵阳市  (相差“市”)
            print(fake.province())#陕西省


            #公司类：
            print("公司类".center(20,"-"))
            print(fake.company())#惠派国际公司信息有限公司
            print(fake.company_suffix())#网络有限公司
            print(fake.company_prefix())#鑫博腾飞

            #个人信息类
            print("个人信息类".center(20,"-"))
            print(fake.name())#东浩
            print(fake.simple_profile())
            #{'username': 'leihan', 'name': '武帅', 'sex': 'F', 'address': '吉林省淮安市双滦家街C座 210434', 'mail': 'lishao@hotmail.com', 'birthdate': '1988-11-12'}
            print(fake.user_name(),fake.password(special_chars=False))#ajiang zI2QbHy02p

            #文章类
            print("文章类".center(20,"-"))
            print(fake.word())#当前
            print(fake.words(3))#['欢迎', '支持', '图片']
            print(fake.sentence(3))#精华有关一些.
            print(fake.paragraph())#大家电话空间一起操作图片要求.上海发展到了之间用户也是的人.必须记者关系介绍注册.用户时候投资发布.

    """

    """
    地址信息类：
    fake.address()：完整地址，比如海南省成市丰都深圳路p座 425541
    fake.street_address()：街道+地址，比如兴城路A座
    fake.street_name()：街道名，比如宜都街
    fake.city_name()：城市名,比如兰州
    fake.city()：城市,比如兰州市
    fake.province()：省份名,比如陕西省
    fake.postcode()：邮编
    fake.country()：国家

    公司信息类：
    fake.company()：公司名，比如惠派国际公司信息有限公司
    fake.company_suffix()：公司名后缀(公司性质)，比如网络有限公司
    fake.company_prefix()：公司名前缀，比如鑫博腾飞

    日期类：
    fake.date(pattern="%Y-%m-%d", end_datetime=None)
    fake.year()：随机年份
    fake.day_of_week()：随机星期数
    fake.time(pattern="%H:%M:%S", end_datetime=None)：随机时间

     网络类：
    fake.company_email()：企业邮箱
    fake.email():邮箱

    个人信息类：
    fake.name()：姓名
    fake.user_name(*args, **kwargs)：用户名，只是随机的英文姓名组合，一般是6位
    fake.phone_number()：电话号码
    fake.simple_profile(sex=None)：简略个人信息，包括用户名，姓名，性别，地址，邮箱，出生日期。比如{'username': 'chao', 'name': '胡秀兰', 'sex': 'M', 'address': '宁夏回族自治区玉市沙湾宁德路t座 873713', 'mail': 'uxiao@yahoo.com', 'birthdate': '1998-06-12'}
    fake.profile(fields=None, sex=None)：详略个人信息，比简略个人信息多出公司名、血型、工作、位置、域名等等信息。
    fake.password()：密码
    参数选项：length：密码长度；special_chars：是否能使用特殊字符；digits：是否包含数字；upper_case：是否包含大写字母；lower_case：是否包含小写字母。
    默认情况：length=10, special_chars=True, digits=True, upper_case=True, lower_case=True
    fake.job()：工作


    文章类：
    fake.word(ext_word_list=None)：随机词语
    ext_word_list可以是一个列表，那么词语会从列表中取
    fake.words(nb=3, ext_word_list=None)：随机多个词语
    nb是数量，对于words来说是返回多少个词语
    fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)：随机短语（会包括短语结束标志点号）
    fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)：随机段落
    fake.paragraphs(nb=3, ext_word_list=None)：多个随机段落


    数据类型类：
    fake.pystr(min_chars=None, max_chars=20)：自定义长度的随机字符串
    fake.pyint():随机整数
    """

fake = Faker(locale='zh_CN')

# 地址
fake.address()  # 完整地址，比如海南省成市丰都深圳路p座 425541
fake.street_address()  # 街道+地址，比如兴城路A座
fake.street_name()  # 街道名，比如宜都街
fake.city_name()  # 城市名,比如兰州
fake.city()  # 城市,比如兰州市
fake.province()  # 省份名,比如陕西省
fake.postcode()  # 邮编
fake.country()  # 国家

# 公司信息类
fake.company()  # 公司名，比如惠派国际公司信息有限公司
fake.company_suffix()  # 公司名后缀(公司性质)，比如网络有限公司
fake.company_prefix()  # 公司名前缀，比如鑫博腾飞

# 日期类

