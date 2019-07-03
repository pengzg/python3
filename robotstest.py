from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url('https://www.jianshu.com')
rp.read()
print(rp.can_fetch('*', 'https://www.360.com/p/aa.html'))