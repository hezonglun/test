import telnetlib
import time
tn = telnetlib.Telnet(host='172.16.0.1',port=23,timeout=10)	# 打开一个连接
tn.set_debuglevel(0)			# 设置调试级别

tn.read_until(b'Username:')		# 读取指定的内容（读取和写入的都必须是字节类型）
tn.write(b'he' + b'\n')		# 写入

tn.read_until(b'Password:')
tn.write(b'123.com' + b'\n')

tn.read_until(b'<he>')
tn.write(b'screen-length 0 temporary' + b'\n')  #设置指定终端屏幕的临时显示行数

tn.read_until(b'<he>')
tn.write(b'system-view' + b'\n')

tn.read_until(b'[he]')
tn.write(b'int lo 1' + b'\n')

tn.read_until(b'[he-LoopBack1]')
tn.write(b'ip add 1.1.1.1 32' + b'\n')


time.sleep(1)
print(tn.read_very_eager().decode('utf8'))		# 读取输出的所有信息
shuru = input()
tn.write(bytes(shuru,encoding='utf8')+b'\n')
tn.close()
