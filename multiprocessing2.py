import subprocess
from multiprocessing import Process, Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end-start)))

def run_proc(name):
    print('Run child proess %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('$ nolookuo')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('utf-8'))
    print('Exit code:', p.returncode)
  #  print('$ nslookup www.python.org')
 #   r = subprocess.call('ls')
#    print('Exit code:', r)

#    print('Parent Process %s.' % os.getpid())
#    p = Pool(7)
#    for i in range(5):
#        p.apply_async(long_time_task, args=(i,))
#    print('Waiting for all subprocesses done...')
#    p.close()
#    p.join()
#    print('ALl done')
   # p = Process(target=run_proc, args=('test',))
#    print('Child process will start.')
#   p.start()
#    p.join()
#    print('CChild process end.')
