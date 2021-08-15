import psutil,os,sys,time,platform

def clear():
    os.system("clear")

def OS_check():
    if (platform.system().lower() != "linux"):
        print("Only Linux OS Supported!")
        time.sleep(0.50)
        exit(0)

def kill_process_pid(process_pid):
    try:
        print("%-9s %-7s %-13s %s" % (9*'',"PID", "name", "path"))
        print("%-9s %-7s %-13s %s" % (9*"",4*'-',5*'-',5*'-'))
        for proc in psutil.process_iter(['open_files', 'name']):
            if (proc.pid == int(process_pid)):
                for paths in proc.info['open_files']:
                    print("%-9s %-7s %-13s %s" % ("Killed:", proc.pid, proc.info['name'], paths.path))
                    proc.kill()
    except PermissionError:
        print("Permission Denied")
        exit(0)
    finally:
        clear()
        for p in psutil.net_connections():
            if (p.pid == int(process_pid)):
                proc = psutil.Process(int(process_pid))
                print("%-9s %s" % (9*'',"PID"))
                print("%-9s %s" % (9*'',4*"-"))
                print("%-9s %s" % ("Killed:", p.pid))
                proc.kill()

def kill_process_name(process_name):
    try:
        print("%-9s %-7s %-13s %s" % (9*'',"PID", "name", "path"))
        print("%-9s %-7s %-13s %s" % (9*"",4*'-',5*'-',5*'-'))
        for proc in psutil.process_iter(['name','open_files']):
            if (proc.info['name'] == process_name):
                for paths in proc.info['open_files']:
                    print("%-9s %-7s %-13s %s" % ("Killed:", proc.pid, proc.info['name'], paths.path))
                    proc.kill()
    except PermissionError:
        print("Permission Denied")
        exit(0)

def network():
    try:
        print("%-7s %-42s %-10s %-42s %-10s %-15s %s" % ("PID", "laddr", 'lport', 'raddr', 'rport', 'status', 'name'))
        print("%-7s %-42s %-10s %-42s %-10s %-15s %s" % (4*"-", 6*"-", 6*"-", 6*"-", 6*"-", 7*"-", 5*"-"))
        for p in psutil.net_connections():
            try:
                print("%-7s %-42s %-10s %-42s %-10s %-15s %s" % (p.pid, p.laddr.ip, p.laddr.port, p.raddr.ip, p.raddr.port, p.status, psutil.Process(p.pid).name()))
            except:
                print("%-7s %-42s %-10s %-42s %-10s %-15s %s" % (p.pid, p.laddr.ip, p.laddr.port, "NONE", "NONE", p.status, psutil.Process(p.pid).name()))
    except:
        pass

def network_pid(pid):
    try:
        print("%-7s %-42s %-10s %-42s %-10s %-15s %s" % ("PID", "laddr", 'lport', 'raddr', 'rport', 'status', 'name'))
        print("%-7s %-42s %-10s %-42s %-10s %-15s %s" % (4*"-", 6*"-", 6*"-", 6*"-", 6*"-", 7*"-", 5*"-"))
        for p in psutil.net_connections():
            if (p.pid == int(pid)):
                try:
                    print("%-7s %-42s %-10s %-42s %-10s %-15s %s" % (p.pid, p.laddr.ip, p.laddr.port, p.raddr.ip, p.raddr.port, p.status, psutil.Process(p.pid).name()))
                except:
                    print("%-7s %-42s %-10s %-42s %-10s %-15s %s" % (p.pid, p.laddr.ip, p.laddr.port, "NONE", "NONE", p.status, psutil.Process(p.pid).name()))
    except:
        pass


def netstat():
    try:
        print("%-6s %-8s %-10s %-13s %s" % ("PID",'user', "status", "name", "path"))
        print(4*"-"+"   "+5*"-"+"    "+7*"-"+"    "+5*"-"+"         "+5*"-")
        for p in psutil.process_iter(['status', 'username', 'name', 'open_files']):
            for file in p.info['open_files'] or []:
                print("%-6s %-8s %-10s %-13s %s" % (p.pid, p.info['username'], p.info['status'], p.info['name'][:10], file.path))
    except Exception as Error:
        print(f"netstat Error: {Error}")
        exit(0)

def netstat_name(name):
    try:
        print("%-6s %-8s %-10s %-13s %s" % ("PID",'user', "status", "name", "path"))
        print(4*"-"+"   "+5*"-"+"    "+7*"-"+"    "+5*"-"+"         "+5*"-")
        for p in psutil.process_iter(['status', 'username', 'name', 'open_files']):
            for file in p.info['open_files'] or []:
                if (p.info['name'] == name):
                    print("%-6s %-8s %-10s %-13s %s" % (p.pid, p.info['username'], p.info['status'], p.info['name'][:10], file.path))
    except Exception as Error:
        print(f"netstat Error: {Error}")
        exit(0)

def netstat_pid(pid):
    try:
        print("%-6s %-8s %-10s %-13s %s" % ("PID",'user', "status", "name", "path"))
        print(4*"-"+"   "+5*"-"+"    "+7*"-"+"    "+5*"-"+"         "+5*"-")
        for p in psutil.process_iter(['status', 'username', 'name', 'open_files']):
            for file in p.info['open_files'] or []:
                if (p.pid == int(pid)):
                    print("%-6s %-8s %-10s %-13s %s" % (p.pid, p.info['username'], p.info['status'], p.info['name'][:10], file.path))
    except Exception as Error:
        print(f"netstat Error: {Error}")
        exit(0)

def pid_info(pid):
    try:
        proc = psutil.Process(int(pid))
        print("%-6s %-8s %s" % ("PID", "name", "status"))
        print("%-6s %-8s %s" % (4*"-", 5*"-", 8*"-"))
        print("%-6s %-8s %s" % (proc.pid, proc.name(), proc.status()))
    except Exception as Error:
        print(f"pid info Error: {Error}")

def main():
    clear()
    try:
        test = sys.argv[1]
        if (test == "-h" or test == "--help"):
            print("Usage:\n   -nk   --network       <Show Network traffic>\n   -n    --netstat       <Show Process traffic>\n   -nn   --netstatname   <Show Process traffic by name>\n   -nkp  --networkpid    <Show Network traffic by pid>\n   -np   --netstatpid    <Show Process traffic by pid>\n   -kn   --killname      <kill process by name>\n   -kp   --killpid       <Kill process by pid>\n   -pi   --pidinfo       <Show pid info>")
    except:
        print("Usage:\n   -nk   --network       <Show Network traffic>\n   -n    --netstat       <Show Process traffic>\n   -nn   --netstatname   <Show Process traffic by name>\n   -nkp  --networkpid    <Show Network traffic by pid>\n   -np   --netstatpid    <Show Process traffic by pid>\n   -kn   --killname      <kill process by name>\n   -kp   --killpid       <Kill process by pid>\n   -pi   --pidinfo       <Show pid info>")

    try:
        if ('-pi' in sys.argv or '--pidinfo' in sys.argv):
            for i in range(len(sys.argv)):
                if (sys.argv[i] == '-pi' or sys.argv[i] == '--pidinfo'):
                    i+=1
                    pid_info(sys.argv[i])
                    break
        else:
            pass
    except:
        pass

    try:
        if ('-nk' in sys.argv or '--network' in sys.argv):
            for i in range(len(sys.argv)):
                if (sys.argv[i] == '-nk' or sys.argv[i] == '--network'):
                    i+=1
                    network()
                    break
        else:
            pass
    except:
        pass

    try:
        if ('-nkp' in sys.argv or '--networkpid' in sys.argv):
            for i in range(len(sys.argv)):
                if (sys.argv[i] == '-nkp' or sys.argv[i] == '--networkpid'):
                    i+=1
                    network_pid(sys.argv[i])
                    break
        else:
            pass
    except:
        pass

    try:
        if ('-n' in sys.argv or '--netstat' in sys.argv):
            for i in range(len(sys.argv)):
                if (sys.argv[i] == '-n' or sys.argv[i] == '--netstat'):
                    i+=1
                    netstat()
                    break
        else:
            pass
    except:
        pass

    try:
        if ('-nn' in sys.argv or '--netstatname' in sys.argv):
            for i in range(len(sys.argv)):
                if (sys.argv[i] == '-nn' or sys.argv[i] == '--netstatname'):
                    i+=1
                    netstat_name(sys.argv[i])
                    break
        else:
            pass
    except:
        pass

    try:
        if ('-np' in sys.argv or '--netstatpid' in sys.argv):
            for i in range(len(sys.argv)):
                if (sys.argv[i] == '-np' or sys.argv[i] == '--netstatpid'):
                    i+=1
                    netstat_pid(sys.argv[i])
                    break
        else:
            pass
    except:
        pass

    try:
        if ('-kn' in sys.argv or '--killname' in sys.argv):
            for i in range(len(sys.argv)):
                if (sys.argv[i] == '-kn' or sys.argv[i] == '--killname'):
                    i+=1
                    kill_process_name(sys.argv[i])
                    break
        else:
            pass
    except:
        pass

    try:
        if ('-kp' in sys.argv or '--killpid' in sys.argv):
            for i in range(len(sys.argv)):
                if (sys.argv[i] == '-kp' or sys.argv[i] == '--killpid'):
                    i+=1
                    kill_process_pid(sys.argv[i])
                    break
        else:
            pass
    except:
        pass

OS_check()
main()
